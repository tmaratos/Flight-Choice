from pathlib import Path
import re

p = Path(r"C:\Flight Choice\index.html")
t = p.read_text(encoding="utf-8")

# Hero
if "hero-vignette" not in t:
    t = t.replace(
        '<motion class="hero-shade" aria-hidden="true"></motion>',
        '<div class="hero-shade" aria-hidden="true"></div>\n      <div class="hero-vignette" aria-hidden="true"></div>',
    )
    t = t.replace('<div class="hero-shade" aria-hidden="true"></div>', '<div class="hero-shade" aria-hidden="true"></motion>', 1)
    t = t.replace('</motion>', '</div>', 1) if '</motion>' in t else t
    if "hero-vignette" not in t:
        t = t.replace(
            '<div class="hero-shade" aria-hidden="true"></div>',
            '<div class="hero-shade" aria-hidden="true"></div>\n      <div class="hero-vignette" aria-hidden="true"></div>',
            1,
        )

t = t.replace(
    "<h1>Knoxville's Premier Private Aircraft Charter and Management Service</h1>",
    '<h1 class="hero-reveal hero-reveal--1">Knoxville\'s Premier Private Aircraft Charter and Management Service</h1>',
)
t = t.replace(
    'class="hero-sub"',
    'class="hero-sub hero-reveal hero-reveal--2"',
    1,
)
t = t.replace('<motion class="hero-btns">', '<div class="hero-btns hero-reveal hero-reveal--3">', 1)
t = t.replace('<motion class="hero-btns">', '<div class="hero-btns hero-reveal hero-reveal--3">', 1)
t = t.replace('class="hero-btns"', 'class="hero-btns hero-reveal hero-reveal--3"', 1)
t = t.replace('class="trust-strip"', 'class="trust-strip hero-reveal hero-reveal--5"', 1)

# Services strip
if "services-strip" not in t:
    t = re.sub(
        r'<div class="pillar-grid--3" style="margin-top:2rem;">.*?</motion>\s*<p style="text-align:center;margin-top:1.5rem;">',
        '''<nav class="services-strip" style="margin-top:3rem;" aria-label="Services overview">
          <a href="services.html#charter">
            <h3>On-Demand Air Charter</h3>
            <p>Your schedule, your route—no connections, no security lines, no waiting.</p>
            <span class="link-arrow">Explore Charter</span>
          </a>
          <a href="services.html#management">
            <h3>Aircraft Management</h3>
            <p>Turn-key ownership with pro-pilots, scheduling, and on-site maintenance support.</p>
            <span class="link-arrow">Explore Management</span>
          </a>
          <a href="services.html#maintenance">
            <h3>Aircraft Maintenance</h3>
            <p>A&amp;P and IA mechanics keeping your aircraft mission-ready under one roof.</p>
            <span class="link-arrow">Explore Maintenance</span>
          </a>
        </nav>
        <p class="section-cta">''',
        t,
        count=1,
        flags=re.DOTALL,
    )
    t = t.replace(
        '<p style="text-align:center;margin-top:1.5rem;"><a href="services.html"',
        '<p class="section-cta"><a href="services.html"',
    )

# Compare
if "compare-editorial" not in t:
    t = t.replace(
        '''        <div class="reveal">
          <p class="eyebrow">Travel Your Way</p>
          <h2 id="compare-h" class="h2">Skip the Terminal. Fly on Your Schedule.</h2>
        </div>
        <motion class="compare-grid reveal">''',
        '''        <div class="compare-editorial reveal">
          <div class="section-head">
            <p class="eyebrow">Travel Your Way</p>
            <h2 id="compare-h" class="h2">Skip the Terminal. Fly on Your Schedule.</h2>
            <ul class="compare-list" style="margin-top:1.5rem;">
              <li>No connections, no security lines, no waiting</li>
              <li>Direct regional access on your itinerary</li>
            </ul>
          </div>
          <div class="compare-grid img-edge-fade reveal">''',
    )
    t = t.replace(
        '''        </div>
        <ul class="compare-list reveal" style="margin-top:2rem;">
          <li>No connections, no security lines, no waiting</li>
          <li>Direct regional access on your itinerary</li>
        </ul>''',
        "        </motion>",
    )
    t = t.replace("</motion>", "</div>", 1)
    t = t.replace(
        "        </motion>\n      </motion>",
        "          </div>\n        </div>",
    )

# Fleet showcase
if "fleet-showcase" not in t:
    fleet_block = '''        <motion class="section-head section-head--center reveal">
          <p class="eyebrow">Aircraft</p>
          <h2 id="fleet-prev" class="h2">High-Performance Beechcraft Fleet</h2>
          <p class="lead">King Air 250, King Air 90, and Baron 58—matched to your mission profile.</p>
        </div>
        <div class="fleet-showcase">
          <article class="aircraft-card fleet-feature reveal">
            <div class="aircraft-card__img img-zoom"><img src="assets/images/fleet/kingair-front-prop-running.webp" alt="King Air 250" loading="lazy"></div>
            <div class="aircraft-card__body">
              <span class="stat-chip">Up to 8 + 2 passengers</span><span class="stat-chip">280+ KTAS</span>
              <h3>King Air 250 Series</h3>
              <p class="desc">Pressurized turboprop with executive cabin comfort.</p>
              <a href="aircraft.html#kingair-250" class="link-arrow">View Aircraft</a>
            </div>
          </article>
          <article class="aircraft-card reveal">
            <div class="aircraft-card__img img-zoom"><img src="assets/images/fleet/kingair-front-quarter-prop-blur.webp" alt="King Air 90" loading="lazy"></div>
            <div class="aircraft-card__body">
              <span class="stat-chip">Up to 6 + 2</span>
              <h3>King Air 90 Series</h3>
              <p class="desc">Proven versatility for regional legs.</p>
              <a href="aircraft.html#kingair-90" class="link-arrow">View Aircraft</a>
            </div>
          </article>
          <article class="aircraft-card reveal">
            <div class="aircraft-card__img img-zoom"><img src="assets/images/fleet/baron-front-ramp-clouds.webp" alt="Baron 58" loading="lazy"></div>
            <div class="aircraft-card__body">
              <span class="stat-chip">Up to 5 passengers</span>
              <h3>Baron 58 Series</h3>
              <p class="desc">Twin-engine efficiency and runway flexibility.</p>
              <a href="aircraft.html#baron-58" class="link-arrow">View Aircraft</a>
            </div>
          </article>
        </motion>
        <p class="section-cta reveal"><a href="aircraft.html" class="btn btn-ghost">Explore Full Fleet &amp; Specs</a></p>'''
    fleet_block = fleet_block.replace("<motion", "<motion").replace("</motion>", "</motion>")
    fleet_block = fleet_block.replace("<motion", "<div").replace("</motion>", "</motion>")
    fleet_block = fleet_block.replace("</motion>", "</div>")

    t = re.sub(
        r'<motion class="reveal" style="text-align:center;max-width:36rem;margin:0 auto 2\.5rem;">.*?Explore Full Fleet &amp; Specs</a></p>',
        fleet_block,
        t,
        count=1,
        flags=re.DOTALL,
    )

t = t.replace('class="safety-callout" style="padding:1.75rem;"', 'class="safety-preview-block"')
t = t.replace(
    'style="text-align:center;max-width:32rem;margin:0 auto;"',
    "",
    1,
)
t = t.replace(
    '<section class="section" aria-labelledby="team-teaser">',
    '<section class="section team-teaser-section" aria-labelledby="team-teaser">',
)
t = t.replace('class="subscribe-box"', 'class="subscribe-box subscribe-editorial"', 1)

t = t.replace("<motion", "<div").replace("</motion>", "</motion>")
t = re.sub(r"</motion>", "</div>", t)

p.write_text(t, encoding="utf-8")
print("done")
