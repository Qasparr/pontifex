#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — server.py — the loopback JSON API
# v0.3.0 "The Third Span"
#
# Epigraph: "If I have seen further it is by standing on the shoulders
# of Giants." — Isaac Newton, 1676.
#
# Thelemic date: ☉ in 14° 54′ Libra, ☽ in 14° 12′ Virgo, dies jovis,
# Anno V:xii e.n. (2026-10-08)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The name PONTIFEX ("bridge-builder") was proposed by the scribe and approved
# by the author's red pen, 2026-10-07. The doctrine is the author's; the
# mechanisms are not.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   (The full statement stands in pontifex/engine.py; this module is the same
#   engine behind a loopback socket — the instrument, networked to itself.)
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The PONTIFEX JSON API over HTTP.

DOCTRINE: loopback only. The server binds 127.0.0.1 (or localhost) and
refuses anything else — the instrument serves its own machine, never the
wire. (The author's standing doctrine, as in the oz enclave and bleat.)

Endpoints (all GET, all JSON):
  /                      — index: name, version, endpoints
  /systems               — the weighing systems and their provenance
  /weigh?word=..&system=..                      — weigh a word
  /bridge?word1=..&system1=..&word2=..&system2=.. — check a convergent point
  /fallback?word=..                             — Hebrew fallback weighing
  /music?tune=..                                — weigh a melody
  /selftest                                     — verify the instrument

MECHANISM: stdlib only (http.server) — no dependencies, the author's
constraint for the core tools.
"""

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

from . import __version__
from .engine import (
    SYSTEMS, weigh, weigh_via_hebrew_fallback, bridge, to_jsonable,
    engine_checks,
)
from .music import weigh_melody


def _ok(data):
    # MECHANISM: every success carries ok:true and the payload — one shape
    # for every endpoint, so clients parse once.
    return 200, {'ok': True, 'data': data}


def _err(message, code=400):
    # MECHANISM: every failure carries ok:false and the reason — never a bare
    # stack trace over the wire.
    return code, {'ok': False, 'error': message}


def route(path, query):
    """Route a request. Returns (status_code, payload_dict). Pure function.

    MECHANISM: routing is pure — no sockets here — so the self-test can
    exercise every endpoint without binding a port.
    """
    try:
        if path == '/':
            return _ok({
                'name': 'PONTIFEX',
                'subtitle': 'the Universal Language Gematria Cartographer',
                'version': __version__,
                'endpoints': ['/systems', '/weigh', '/bridge', '/fallback',
                              '/music', '/selftest'],
            })
        if path == '/systems':
            return _ok({name: spec['provenance']
                        for name, spec in sorted(SYSTEMS.items())})
        if path == '/weigh':
            word, system = query.get('word'), query.get('system')
            if not word or not system:
                return _err('need ?word=..&system=..')
            return _ok(to_jsonable(weigh(word, system)))
        if path == '/bridge':
            need = ('word1', 'system1', 'word2', 'system2')
            if not all(query.get(k) for k in need):
                return _err('need ?word1=..&system1=..&word2=..&system2=..')
            b = bridge(query['word1'], query['system1'],
                       query['word2'], query['system2'])
            return _ok({
                'a': to_jsonable(b['a']),
                'b': to_jsonable(b['b']),
                'convergent': b['convergent'],
                'standing': b['standing'],
            })
        if path == '/fallback':
            word = query.get('word')
            if not word:
                return _err('need ?word=..')
            return _ok(to_jsonable(weigh_via_hebrew_fallback(word)))
        if path == '/music':
            tune = query.get('tune')
            if not tune:
                return _err('need ?tune=..')
            return _ok(to_jsonable(weigh_melody(tune)))
        if path == '/selftest':
            results = [
                {'check': name, 'pass': passed, 'got': repr(got)}
                for name, passed, got in engine_checks()
            ]
            all_ok = all(r['pass'] for r in results)
            return _ok({'all_pass': all_ok, 'checks': results})
        return _err('unknown endpoint: %s' % path, 404)
    except ValueError as e:
        # MECHANISM: engine errors (unknown system) become 400s, not 500s —
        # the request was wrong, not the instrument.
        return _err(str(e), 400)
    except Exception as e:  # noqa: BLE001 — the wire never sees a traceback
        return _err('internal error: %s' % e, 500)


class Handler(BaseHTTPRequestHandler):
    """HTTP handler — thin skin over route()."""

    def log_message(self, *args):
        # MECHANISM: quiet by default — the server is infrastructure, not
        # the show. (Uncomment to debug.)
        pass

    def _send(self, code, payload):
        body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        # MECHANISM: parse, flatten single-value params, route, send.
        parsed = urlparse(self.path)
        query = {k: v[0] for k, v in parse_qs(parsed.query).items()}
        code, payload = route(parsed.path, query)
        self._send(code, payload)


def serve(host='127.0.0.1', port=8077):
    """Serve the JSON API. Returns an exit code (0 ok, 1 failure).

    DOCTRINE: loopback only — host must be 127.0.0.1 or localhost, else we
    refuse to start. The instrument serves its own machine, never the wire.
    """
    # MECHANISM: the doctrine is enforced, not suggested — a non-loopback
    # bind is a hard refusal, exit 1.
    if host not in ('127.0.0.1', 'localhost', '::1'):
        print('refused: PONTIFEX serves loopback only (got host=%r)' % host)
        return 1
    server = ThreadingHTTPServer((host, port), Handler)
    print('PONTIFEX %s serving on http://%s:%d (loopback only) — Ctrl-C to stop'
          % (__version__, host, port))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
