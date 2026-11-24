#!/usr/bin/env python3
# =============================================================================
# PONTIFEX — pentadic.py — THE PENTADIC NOTATION SEAT: a reader for
# the Scandinavian calendar notation. NOT a weighing bank, and NOT
# a runic letter table — the field audit found none, in either the
# runes or Ogham (THE-RUNIC-AND-OGHAM-FIELD.md).
#
# Epigraph: "The notation is similar to the older Roman numerals
# for numbers up to 9 (I–VIIII). Unlike the Roman notation, the
# ticks are placed vertically on a stem or stav of the rune." —
# Wikipedia, "Pentadic numerals" (read entire, 2026-11-24).
#
# Thelemic date: ☉ in Sagittarius, dies Martis, Anno V:xii e.n.
# (2026-11-24)
#
# 93.
#
# Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
# The doctrine is the author's; the mechanisms are the scribe's,
# open to the author's red pen.
#
# SCIENTIFIC ILLUMINISM — hypothesis → method → observation → result:
#   Hypothesis (the field audit's gate, THE-RUNIC-AND-OGHAM-
#     FIELD.md §IX): the western field offers, beside its checked
#     negative, one NOTATION — the pentadic stave notation of the
#     Scandinavian calendars — whose sign law two witnesses state
#     identically. A reader door is the honest seat: it parses the
#     notation and returns the number; it must never register as a
#     weigh() system, because no runic or Ogham letter-value table
#     exists (the closure proven by the audit, battery 20/20).
#   Method: the sign law is the audit's, transcribed from two
#     witnesses (Wikipedia, "Pentadic numerals"; Wikipedia, "Runic
#     calendar") and frozen in research/western-sweep/
#     pentadic-notation.csv; the law is verified against the
#     witnesses' stated extent in pentadic_checks() below, and
#     parity against the frozen CSV is proven by
#     test_pentadic_parity.py at the repository root.
#   Observation: recorded in the audit document.
#   Result: a reader, fenced as a reader.
#
# All Rights Reserved, Without Prejudice.
# "Live, Love, and let Love, Live."
# =============================================================================
"""Read pentadic numerals in the attested calendar notation.

DOCTRINE — WHAT THIS SEAT IS AND IS NOT: this module READS the
pentadic stave notation — ticks and five-signs on a stem, the
notation of the Scandinavian runic calendars (clogs) — and returns
the number the notation denotes. It is not a gematria bank: the
runes are not letters with values here (the golden-number labels
of the older calendars are a closed cycle's coordinates, frozen
in the audit, not read here), and no weigh() system is registered
here. A text that is not a canonical numeral of the notation is
refused with an error, never silently misread — a reader that
guesses is a forger.

THE INPUT CONVENTION (stated on the seat, as the Chinese reader
states its dresses): the notation is graphic — strokes on a stem —
so the reader takes a per-sign transcription in the witnesses' own
shapes: 'i' is one tick (a horizontal line on the stem); 'u' is
the five-sign, which the witnesses describe as "what looks like an
inverted letter U"; two five-signs opposing ('uu') are the
ten-sign, a single sign in the notation, not two fives added. A
numeral is, in canonical order: an optional ten-sign ('uu', at
most two — the second makes twenty), then an optional unit sign:
'i'×1–4, or 'u', or 'u' followed by 'i'×1–4. The notation is
purely additive — it has no subtractive form (the witnesses
compare it to the additive Roman I–VIIII, not to IV).

THE EXTENT: the witnesses bound the notation's calendar use at
the golden numbers, 1–19, "or even 20". The reader seats 1–20 and
refuses beyond: a reader that extrapolates past its witnesses'
extent is minting law, not reading notation.

NOT SEATED: the positional digit stratum (Edward Larsson's notes,
1885 — the oldest authenticated use of pentadic runes as a base-ten
positional digit set; the North American stones that use it are
modern hoaxes in the consensus both witnesses print). Its
per-digit shapes live in the witnesses' images and in prose
descriptions that part; no digit table is frozen, and this reader
does not seat the stratum. See the audit, §IV.
"""


def _read_unit(text):
    """One unit sign: ticks, the five-sign, or five-sign + ticks.

    MECHANISM: 'i'×1–4 reads its count; 'u' reads 5; 'u' followed
    by 'i'×1–4 reads 5 + count. Anything else — ticks before the
    five-sign, more than four ticks — is not a sign of this
    notation and raises."""
    if not text:
        return 0
    if text[0] == 'u':
        ticks = text[1:]
        if ticks and (set(ticks) != {'i'} or len(ticks) > 4):
            raise ValueError('not a pentadic unit sign: %r' % text)
        return 5 + len(ticks)
    if set(text) == {'i'} and len(text) <= 4:
        return len(text)
    raise ValueError('not a pentadic unit sign: %r' % text)


def read_pentadic(text):
    """Read a pentadic numeral in the attested calendar notation.

    MECHANISM: count the leading ten-signs — each 'uu' at the head
    is one ten-sign (the witnesses' single sign of two opposing
    five-signs); at most two stand (twenty, the stated ceiling);
    the remainder must be one unit sign. Returns a result dict:
    the text as given, the number, the per-sign breakdown (sign
    and role), and the notation's name. A form outside the
    canonical grammar raises ValueError: the reader refuses what
    it cannot read.
    """
    if not isinstance(text, str) or not text:
        raise ValueError('not a pentadic numeral: %r' % (text,))
    if set(text) - {'i', 'u'}:
        raise ValueError('not a pentadic numeral: %r' % text)
    breakdown = []
    rest = text
    tens = 0
    while rest.startswith('uu') and tens < 2:
        breakdown.append(('uu', 'ten-sign'))
        rest = rest[2:]
        tens += 1
    if rest.startswith('uu'):
        raise ValueError('beyond the notation\'s extent: %r' % text)
    unit = _read_unit(rest)
    if rest:
        breakdown.append((rest, 'unit-sign'))
    value = 10 * tens + unit
    if value < 1 or value > 20:
        raise ValueError('beyond the notation\'s extent 1–20: %r'
                         % text)
    return {
        'text': text,
        'value': value,
        'breakdown': breakdown,
        'notation': 'pentadic',
    }


def pentadic_checks():
    """Verify the notation seat against the witnesses' law.

    MECHANISM: the sign law recomputed at its coordinates (the
    tick group, the five-sign as a single sign, the ten-sign as a
    single sign), the golden-number extent read entire (every
    value 1–19 in canonical form, and 20), and the refusals: a
    non-canonical form raises, it does not misread. Parity against
    the frozen CSV is proven separately by test_pentadic_parity.py.
    """
    checks = []

    def canon(n):
        # the canonical transcription of n under the frozen law
        tens, unit = divmod(n, 10)
        s = 'uu' * tens
        if unit >= 5:
            s += 'u' + 'i' * (unit - 5)
        elif unit:
            s += 'i' * unit
        return s

    bad = [(n, read_pentadic(canon(n))['value'])
           for n in range(1, 21)
           if read_pentadic(canon(n))['value'] != n]
    checks.append(('the extent reads entire: every value 1–20 in '
                   'canonical form reads itself', not bad,
                   bad or '20/20 exact'))
    checks.append(('the five-sign is one sign at 5: '
                   "read_pentadic('u') == 5 with one breakdown row",
                   read_pentadic('u')['value'] == 5
                   and read_pentadic('u')['breakdown']
                   == [('u', 'unit-sign')],
                   read_pentadic('u')))
    checks.append(('the ten-sign is one sign at 10, not two fives: '
                   "read_pentadic('uu') == 10, role ten-sign",
                   read_pentadic('uu')['value'] == 10
                   and read_pentadic('uu')['breakdown']
                   == [('uu', 'ten-sign')],
                   read_pentadic('uu')['breakdown']))
    checks.append(('the golden extent\'s top: 19 == ten + five + '
                   "four ticks ('uuuiiii')",
                   read_pentadic('uuuiiii')['value'] == 19,
                   read_pentadic('uuuiiii')['value']))
    refused = []
    for bad_text in ('iu', 'iiiii', 'uuuuu', 'x', '', 'uuiiiii'):
        try:
            read_pentadic(bad_text)
        except ValueError:
            refused.append(bad_text)
    checks.append(('the refusals: non-canonical forms raise '
                   'ValueError — ticks before the five-sign, five '
                   'ticks, three ten-signs, foreign glyphs, the '
                   'empty string, a sprawled unit', len(refused) == 6,
                   refused))
    return checks

# =============================================================================
# Closing motto: "Live, Love, and let Love, Live."
# 93. All Rights Reserved, Without Prejudice.
# =============================================================================
