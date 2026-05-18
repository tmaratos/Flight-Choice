from pathlib import Path

p = Path(r"C:\Flight Choice\index.html")
t = p.read_text(encoding="utf-8")

COMPARE_OLD = (
    '        <div class="reveal">\n'
    '          <p class="eyebrow">Travel Your Way</p>\n'
    '          <h2 id="compare-h" class="h2">Skip the Terminal. Fly on Your Schedule.</h2>\n'
    "        </div>\n"
    '        <motion class="compare-grid reveal">'
).replace("<motion ", "<div ")

COMPARE_NEW = (
    '        <div class="compare-editorial reveal">\n'
    '          <div class="section-head">\n'
    '            <p class="eyebrow">Travel Your Way</p>\n'
    '            <h2 id="compare-h" class="h2">Skip the Terminal. Fly on Your Schedule.</h2>\n'
    '            <ul class="compare-list">\n'
    "              <li>No connections, no security lines, no waiting</li>\n"
    "              <li>Direct regional access on your itinerary</li>\n"
    "            </ul>\n"
    "          </div>\n"
    '          <div class="compare-grid img-edge-fade">'
)

COMPARE_CLOSE_OLD = (
    '            <img src="assets/images/operations/private-transfer-luggage-to-aircraft.webp" '
    'alt="Private transfer to aircraft" loading="lazy" decoding="async">\n'
    "          </div>\n"
    "        </div>\n"
    "      </div>\n"
    "    </section>\n"
    "\n"
    '    <section class="section section--dark" aria-labelledby="fleet-prev">'
)

COMPARE_CLOSE_NEW = (
    '            <img src="assets/images/operations/private-transfer-luggage-to-aircraft.webp" '
    'alt="Private transfer to aircraft" loading="lazy" decoding="async">\n'
    "          </div>\n"
    "          </div>\n"
    "        </div>\n"
    "      </div>\n"
    "    </section>\n"
    "\n"
    '    <section class="section section--dark" aria-labelledby="fleet-prev">'
)

FLEET_HEAD_OLD = (
    '        <div class="reveal" style="text-align:center;max-width:36rem;margin:0 auto 2.5rem;">\n'
    '          <p class="eyebrow">Aircraft</p>\n'
    '          <h2 id="fleet-prev" class="h2">High-Performance Beechcraft Fleet</h2>\n'
    '          <p class="lead" style="margin:0 auto;">King Air 250, King Air 90, and Baron 58—matched to your mission profile.</p>\n'
    "        </div>\n"
    '        <div class="fleet-cards">'
)

FLEET_HEAD_NEW = (
    '        <motion class="section-head section-head--center reveal">\n'
    '          <p class="eyebrow">Aircraft</p>\n'
    '          <h2 id="fleet-prev" class="h2">High-Performance Beechcraft Fleet</h2>\n'
    '          <p class="lead">King Air 250, King Air 90, and Baron 58—matched to your mission profile.</p>\n'
    "        </div>\n"
    '        <div class="fleet-showcase">'
).replace("<motion ", "<motion ").replace("<motion class", "<div class")

if "compare-editorial" not in t and COMPARE_OLD in t:
    t = t.replace(COMPARE_OLD, COMPARE_NEW)
    if COMPARE_CLOSE_OLD in t:
        t = t.replace(COMPARE_CLOSE_OLD, COMPARE_CLOSE_NEW, 1)

if "fleet-showcase" not in t and FLEET_HEAD_OLD in t:
    t = t.replace(FLEET_HEAD_OLD, FLEET_HEAD_NEW)
    t = t.replace(
        '<article class="aircraft-card reveal">\n'
        '            <motion class="aircraft-card__img"><img src="assets/images/fleet/kingair-front-prop-running.webp"'.replace(
            "<motion ", "<div "
        ),
        '<article class="aircraft-card fleet-feature reveal">\n'
        '            <div class="aircraft-card__img img-zoom"><img src="assets/images/fleet/kingair-front-prop-running.webp"',
        1,
    )
    t = t.replace(
        '<article class="aircraft-card reveal">\n'
        '            <div class="aircraft-card__img"><img src="assets/images/fleet/kingair-front-prop-running.webp"',
        '<article class="aircraft-card fleet-feature reveal">\n'
        '            <motion class="aircraft-card__img img-zoom"><img src="assets/images/fleet/kingair-front-prop-running.webp"'.replace(
            "<motion ", "<div "
        ),
        1,
    )
    t = t.replace('class="aircraft-card__img"><img', 'class="aircraft-card__img img-zoom"><img')
    t = t.replace(
        '<p class="meta">Up to 8 + 2 passengers</p>',
        '<span class="stat-chip">Up to 8 + 2 passengers</span><span class="stat-chip">280+ KTAS</span>',
        1,
    )
    t = t.replace('<p class="meta">Up to 6 + 2 passengers</p>', '<span class="stat-chip">Up to 6 + 2</span>', 1)
    t = t.replace('<p class="meta">Up to 5 passengers</p>', '<span class="stat-chip">Up to 5 passengers</span>', 1)
    t = t.replace(
        '<p style="text-align:center;margin-top:1.5rem;"><a href="aircraft.html"',
        '<p class="section-cta reveal"><a href="aircraft.html"',
        1,
    )

TEAM_OLD = (
    '    <section class="section team-teaser-section" aria-labelledby="team-teaser">\n'
    "      <div class=\"container reveal\" >\n"
    '        <p class="eyebrow">Meet Our Team</p>\n'
    '        <h2 id="team-teaser" class="h2">Experienced People. Reliable Operations.</h2>\n'
    '        <p class="lead" style="margin:0 auto 1.25rem;">'
)
TEAM_NEW = (
    '    <section class="section team-teaser-section" aria-labelledby="team-teaser">\n'
    '      <div class="container reveal">\n'
    '        <div class="section-head section-head--center">\n'
    '          <p class="eyebrow">Meet Our Team</p>\n'
    '          <h2 id="team-teaser" class="h2">Experienced People. Reliable Operations.</h2>\n'
    '          <p class="lead">'
)
TEAM_FOOT_OLD = (
    '        <a href="team.html" class="btn btn-ghost">Meet the Team</a>\n'
    "      </div>\n"
    "    </section>\n"
    "\n"
    '    <section class="section section--dark" aria-labelledby="empty-sub">'
)
TEAM_FOOT_NEW = (
    "        </div>\n"
    '        <p class="section-cta"><a href="team.html" class="btn btn-ghost">Meet the Team</a></p>\n'
    "      </div>\n"
    "    </section>\n"
    "\n"
    '    <section class="section section--dark" aria-labelledby="empty-sub">'
)

if TEAM_OLD in t:
    t = t.replace(TEAM_OLD, TEAM_NEW)
if TEAM_FOOT_OLD in t:
    t = t.replace(TEAM_FOOT_OLD, TEAM_FOOT_NEW, 1)

t = t.replace(' class="h2" style="font-size:1.65rem;"', ' class="h2"', 1)
t = t.replace(
    '<p style="color:var(--text-muted);margin-top:0.75rem;">Your safety',
    '<p class="lead">Your safety',
    1,
)
t = t.replace(' style="display:inline-block;margin-top:1rem;"', '', 1)

p.write_text(t, encoding="utf-8")
print("compare-editorial:", "compare-editorial" in t)
print("fleet-showcase:", "fleet-showcase" in t)
