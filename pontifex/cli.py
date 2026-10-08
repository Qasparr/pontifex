#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — cli.py — the command-line interface, built for scripts
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
#   (The full statement stands in pontifex/engine.py; this module is the
#   instrument's handle — the same engine, shaped for hands and scripts.)
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================

"""The PONTIFEX command-line interface.

DOCTRINE: the CLI is the instrument's handle — the same engine, shaped for
hands and for scripts. Human output shows its work; --json output speaks
machine. Exit codes are a contract:

  0 — success (for `bridge`: the point CONVERGED)
  1 — runtime error (unknown system, bad input, server failure)
  2 — usage error (argparse)
  3 — success, but the `bridge` point DIVERGED (scripts can test $?)

A script that only cares whether the bridge held: `pontifex bridge ... `
and check the exit code. A script that wants the numbers: add --json.
"""

import argparse
import json
import sys

from .engine import (
    SYSTEMS, weigh, weigh_via_hebrew_fallback, bridge, to_jsonable,
    fmt_breakdown, self_test,
)
from .music import weigh_melody, MUSIC_CONVENTIONS
from . import __version__


def _emit_human_weigh(r):
    # MECHANISM: the human shape — value first, then the audit trail, then
    # whatever honesty the result carries (mergers, conventions).
    print('%s [%s, %s] = %d' % (r['word'], r['system'], r['provenance'], r['value']))
    print('  ' + fmt_breakdown(r['breakdown']))
    if r.get('mergers'):
        from .tables import MERGERS
        print('  mergers (distinction lost): %s' % ', '.join(
            '%s <- %s' % (h, '/'.join(MERGERS[h])) for h in r['mergers']))
    elif 'mergers' in r:
        print('  mergers: none — the rendering is lossless')
    if r.get('conventions'):
        print('  conventions:')
        for c in r['conventions']:
            print('    - ' + c)


def _emit(result, as_json):
    # MECHANISM: one gate for both shapes — hands get the audit trail, scripts
    # get the JSON. Same data either way; the shape is the only difference.
    if as_json:
        print(json.dumps(to_jsonable(result), ensure_ascii=False, indent=2))
    else:
        _emit_human_weigh(result)
    return 0


def _error(message, as_json):
    # MECHANISM: errors speak the requested shape too — a script parsing
    # stdout must never choke on a human sentence where JSON was promised.
    if as_json:
        print(json.dumps({'ok': False, 'error': message}, ensure_ascii=False))
    else:
        print('error: %s' % message, file=sys.stderr)
    return 1


def build_parser():
    # MECHANISM: argparse — subcommands per operation, --json global.
    # DOCTRINE: the CLI surface mirrors the Python API one-to-one, so the
    # docs describe both at once (see API.md).
    parser = argparse.ArgumentParser(
        prog='pontifex',
        description='PONTIFEX %s — the Universal Language Gematria '
                    'Cartographer' % __version__,
    )
    parser.add_argument('--json', action='store_true',
                        help='machine-readable JSON output (for scripts)')
    sub = parser.add_subparsers(dest='cmd', required=True)

    p = sub.add_parser('weigh', help='weigh a word in a system')
    p.add_argument('word', help='the word to weigh')
    p.add_argument('system', help='one of: %s' % ', '.join(sorted(SYSTEMS)))

    p = sub.add_parser('bridge', help='check a convergent point between two weighings')
    p.add_argument('word1'); p.add_argument('system1')
    p.add_argument('word2'); p.add_argument('system2')

    p = sub.add_parser('fallback', help='weigh a Latin word via the Hebrew fallback (mergers shown)')
    p.add_argument('word', help='the Latin-script word')

    p = sub.add_parser('music', help='weigh a melody (ABC notation or bare notes)')
    p.add_argument('tune', nargs='+', help='the tune, quoted or bare')

    sub.add_parser('systems', help='list the weighing systems and their provenance')

    sub.add_parser('selftest', help='verify the instrument against the established bridges')

    p = sub.add_parser('serve', help='serve the JSON API on loopback (see API.md)')
    p.add_argument('--port', type=int, default=8077)
    p.add_argument('--host', default='127.0.0.1',
                   help='bind address — loopback only, by doctrine')
    return parser


def main(argv=None):
    # MECHANISM: --json is accepted anywhere on the command line — scripts
    # should not have to care whether it precedes the subcommand. Strip it
    # here so argparse never sees it out of place.
    argv = list(sys.argv[1:] if argv is None else argv)
    as_json = False
    while '--json' in argv:
        argv.remove('--json')
        as_json = True
    args = build_parser().parse_args(argv)
    try:
        if args.cmd == 'weigh':
            return _emit(weigh(args.word, args.system), as_json)
        if args.cmd == 'fallback':
            return _emit(weigh_via_hebrew_fallback(args.word), as_json)
        if args.cmd == 'music':
            return _emit(weigh_melody(' '.join(args.tune)), as_json)
        if args.cmd == 'bridge':
            b = bridge(args.word1, args.system1, args.word2, args.system2)
            if as_json:
                payload = {
                    'a': to_jsonable(b['a']),
                    'b': to_jsonable(b['b']),
                    'convergent': b['convergent'],
                    'standing': b['standing'],
                }
                print(json.dumps(payload, ensure_ascii=False, indent=2))
            else:
                a, c = b['a'], b['b']
                print('%s [%s] = %d   vs   %s [%s] = %d' % (
                    a['word'], a['system'], a['value'],
                    c['word'], c['system'], c['value']))
                print('  convergent: %s — %s' % (b['convergent'], b['standing']))
            # MECHANISM: the exit code IS the verdict — scripts test $?
            # without parsing. 0 = the bridge held, 3 = it diverged.
            return 0 if b['convergent'] else 3
        if args.cmd == 'systems':
            data = {name: spec['provenance'] for name, spec in sorted(SYSTEMS.items())}
            if as_json:
                print(json.dumps(data, ensure_ascii=False, indent=2))
            else:
                for name, prov in data.items():
                    print('%-14s %s' % (name, prov))
            return 0
        if args.cmd == 'selftest':
            ok = self_test()
            if as_json:
                # MECHANISM: re-run quietly for the machine shape — the human
                # printing already happened; scripts get the verdict object.
                print(json.dumps({'ok': ok}, ensure_ascii=False))
            return 0 if ok else 1
        if args.cmd == 'serve':
            from .server import serve
            return serve(host=args.host, port=args.port)
    except ValueError as e:
        # MECHANISM: engine errors (unknown system, ...) are usage-adjacent
        # failures — exit 1, in the requested shape.
        return _error(str(e), as_json)
    except BrokenPipeError:
        # MECHANISM: piping to `head` is not a failure — die quiet.
        return 0


if __name__ == '__main__':
    sys.exit(main())

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
