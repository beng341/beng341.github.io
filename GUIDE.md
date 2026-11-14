# Website Maintenance Guide

A practical reference for maintaining this site (Jekyll + the al-folio theme, deployed to GitHub Pages at `benarmstrong.ca`).

> **Note:** Jekyll publishes any root-level `.md` file without front matter as a static file. To keep this guide off the live site, add `- GUIDE.md` to the `exclude:` list in `_config.yml` (next to `README.md`).

---

## Part 1 — How the site is put together (and what to edit)

### At a glance

| I want to…                         | Edit this                                                        |
| ---------------------------------- | ---------------------------------------------------------------- |
| Change the homepage bio / photo    | `_pages/about.md` (photo lives in `assets/img/`)                 |
| Add or remove a news item          | `_news/` (one file per item)                                     |
| Add or update a paper              | `_bibliography/papers.bib` (+ PDF in `assets/pdf/`)              |
| Mark a paper as "selected"         | Add `selected={true}` to its `.bib` entry                         |
| Edit the teaching page             | `_pages/teaching.md`                                             |
| Update the CV                      | Replace `assets/pdf/strongarms_cv.pdf` (keep the same filename)  |
| Add a new page / header link       | New file in `_pages/` with `nav: true` and a `nav_order`         |
| Change name, email, social icons   | `_config.yml` (top section)                                      |
| Set a paper's badge colour / link  | `pub_type` and `venue_url` fields in its `.bib` entry            |
| Add or change a publication type   | `publication_types` in `_config.yml`                             |
| Link co-author names to their sites | `_data/coauthors.yml`                                           |

### `_config.yml` — site-wide settings

The single most important file. Key fields:

- `first_name`, `last_name`, `title: blank` → the name shown top-left in the navbar.
- `email`, `scholar_userid`, `github_username`, `linkedin_username`, etc. → each one you fill in adds an icon to the bottom of the homepage (because `social: true` in `about.md`). Leave blank/commented to hide.
- `description` → used as the `<meta name="description">` for any page that doesn't set its own (including the homepage). This is what search engines show.
- `url` → the canonical domain. Used in the sitemap, RSS feed, and some absolute links. Should match `CNAME`.
- `announcements.limit` → how many news items show on the homepage (currently 3).
- `scholar:` block → controls how `papers.bib` is rendered (sorting, grouping by year, etc.).
- `max_author_limit` → number of authors shown before "and N more authors".

**Changes to `_config.yml` are NOT picked up by a running `jekyll serve`.** Stop the server and restart it.

### Homepage — `_pages/about.md`

- Front matter (between the `---` lines):
  - `subtitle:` the line under the name (HTML links allowed).
  - `profile.image:` filename in `assets/img/`.
  - `profile.more_info:` HTML shown under the photo.
  - `news: true`, `selected_papers: true`, `social: true` toggle those homepage sections.
- Everything below the second `---` is the bio, written in Markdown.

### News — `_news/`

Each news item is one Markdown file. Filename convention: `YYYY-MM-DD-short-name.md`.

```markdown
---
layout: post
date: 2026-12-09
inline: true
related_posts: false
---

Our paper has been accepted to <a href="https://example.com">Venue</a>!
```

- `inline: true` → the text is shown directly in the news list. **Use this for almost everything.**
- `inline: false` → only a *title* is shown, linking to a separate page for the item. You must then add `title: ...` to the front matter (otherwise Jekyll invents one from the filename, e.g. "Tulane").
- The `date:` in the front matter is what's displayed and used for sorting.
- **Future dates are hidden.** Jekyll skips any item dated after the build time, so a news item dated next week won't appear until the site is rebuilt *after* that date. Date news items today-or-earlier.
- To delete a news item, delete its file.
- Internal links: prefer root-relative paths like `/assets/pdf/file.pdf` rather than `https://benarmstrong.ca/...`.

### Publications — `_bibliography/papers.bib` + `assets/pdf/`

Everything on the publications page comes from `papers.bib`. `_pages/publications.md` runs `{% bibliography %}` (which lists papers grouped by year, newest first) and adds sort/filter controls above it (see "Publication types" below).

To add a paper:

1. Put the PDF in `assets/pdf/`. Simple filenames without spaces are safest (e.g. `NeurIPS-2026-DeepVoting.pdf`).
2. Add an entry to `papers.bib`:

```bibtex
@inproceedings{Armstrong_Example_2026,
  title={Paper Title},
  author={Armstrong, Ben and Coauthor, Firstname},
  booktitle={Proceedings of the 40th Conference on Something},
  year={2026},
  month={12},
  abbr={NeurIPS},
  pub_type={conference},
  venue_url={https://neurips.cc/},
  pdf={NeurIPS-2026-DeepVoting.pdf},
  arxiv={2408.13630},
  abstract={...},
  tldr={One or two plain-language sentences.},
  selected={true}
}
```

How each field is used by the theme (`_layouts/bib.liquid`):

| Field                | Effect                                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------- |
| `author`             | Always `Last, First and Last, First`. A missing comma flips first/last name in the display.               |
| `journal`            | Venue line for `@article` entries.                                                                         |
| `booktitle`          | Venue line for `@inproceedings` entries.                                                                   |
| `publisher`          | **Not displayed.** Don't put the venue here.                                                               |
| `note`               | Shown as an extra line under the venue.                                                                    |
| `abbr`               | Text of the badge on the left (e.g. `NeurIPS`). No `abbr` means no badge.                                  |
| `pub_type`           | Publication type, e.g. `conference`. Sets the badge colour and how the paper is sorted/filtered. Must match a `key` in `publication_types` in `_config.yml`; otherwise the paper counts as "Other" and the badge uses the default theme colour. |
| `venue_url`          | Makes the badge a link to this URL. Omit it for a badge with no link.                                     |
| `pdf`                | "PDF" button. Either a filename in `assets/pdf/` (must include `.pdf` and match exactly) or a full URL.    |
| `arxiv`              | "arXiv" button (just the ID, e.g. `2408.13630`).                                                           |
| `abstract`           | "Abs" button that expands the abstract.                                                                    |
| `tldr`               | "TLDR" button that expands this short summary (works like the abstract; opening one closes the other).    |
| `code`, `slides`, `poster`, `website`, `supp`, `html` | Extra buttons. `slides`/`poster`/`supp` can be filenames in `assets/pdf/` or URLs. |
| `selected={true}`    | Paper also appears under "selected publications" on the homepage.                                         |
| `bibtex_show={true}` | Adds a "Bib" button showing the BibTeX.                                                                    |

Field names are case-sensitive and must be spelled exactly as above (`pub_type`, not `pubtype` or `type`; `type` is reserved by BibTeX).

### Publication types (badge colours, sorting and filtering)

The types are defined once in `_config.yml`:

```yaml
publication_types:
  - key: conference      # the value you write in pub_type={...}
    label: Conference    # shown on the checkbox and as the heading when sorting by type
    color: "#1f4e8c"     # badge background (keep the quotes: # starts a YAML comment)
  - key: journal
    label: Journal
    color: "#7a3e9d"
  - key: workshop
    label: Workshop
    color: "#2e7d6b"
  - key: preprint
    label: Preprint
    color: "#6c757d"
```

On the publications page, visitors can sort by **year** or by **type**, and untick checkboxes to hide types. A type's checkbox only appears if at least one paper has that `pub_type`. Papers with no `pub_type`, or one that isn't in the list, are grouped as **Other** (with their own checkbox). Without JavaScript, the page falls back to the plain list grouped by year.

**To add a new type** (e.g. "thesis"):

1. Add an entry to `publication_types` in `_config.yml`:
   ```yaml
     - key: thesis
       label: Thesis
       color: "#a0522d"
   ```
2. Set `pub_type={thesis}` on the relevant entries in `papers.bib`.
3. Restart `bundle exec jekyll serve` (config changes need a restart).

Related tasks:

- **Change the order of types** when sorting by type: reorder the entries in `publication_types`. "Other" always comes last.
- **Change a colour or label**: edit `color` / `label`. Dark colours work best, since the badge text is white.
- **Rename or remove a type**: change or remove its entry *and* update every `pub_type={...}` that used it; otherwise those papers fall into "Other".

The pieces behind this, in case you need to debug: `_layouts/bib.liquid` (badge, TLDR button, and the `data-pub-type` / `data-year` attributes on each paper), `_pages/publications.md` (the controls), `assets/js/publications.js` (sorting and filtering), and `assets/js/common.js` (Abs/TLDR/Bib toggles).

**Deploy gotcha:** the deploy workflow only triggers on changes to `assets/**`, `*.md`, `*.yml`, `*.liquid`, `*.html`, `*.js`. A commit that *only* changes `papers.bib` will not redeploy. Either commit it together with the PDF / a news item, or trigger the "Deploy site" workflow manually from the repo's Actions tab ("Run workflow").

### CV

`_pages/cv.md` puts the "cv" link in the header. Its `permalink` points straight at `/assets/pdf/strongarms_cv.pdf`, so clicking the link opens the PDF. To update the CV, just overwrite `assets/pdf/strongarms_cv.pdf` with the new file.

### Teaching — `_pages/teaching.md`

Plain HTML/Markdown below the front matter. Copy an existing `<p>...</p>` block to add a course.

### Adding a brand-new page and putting it in the header

Create `_pages/<name>.md`:

```markdown
---
layout: page
title: talks
permalink: /talks/
description: One line shown under the title (also used as the meta description).
nav: true
nav_order: 3
---

Content in Markdown (or HTML) goes here.

## A section heading

- A list item
```

- `title` → text of the header link (al-folio convention is lowercase).
- `permalink` → URL. Always start and end with `/`.
- `nav: true` → appears in the header. `nav: false` → page exists but isn't linked.
- `nav_order` → position in the header (lower = further left). Current order: publications (2), teaching (4), cv (5). "about" is always first.
- `layout: page` → standard page with title and description. `layout: default` → bare page, no title block.

To remove a page from the header without deleting it, set `nav: false`. To delete it entirely, delete the file.

### Images

- Put images in `assets/img/`. `jekyll-imagemagick` automatically generates resized `.webp` versions at build time (requires ImageMagick installed locally).
- In a page, use the theme's include for responsive images:
  `{% include figure.liquid path="assets/img/photo.jpg" class="img-fluid rounded" %}`

### Things you normally don't touch

| Folder                   | What it is                                                                       |
| ------------------------ | -------------------------------------------------------------------------------- |
| `_layouts/`              | Page templates (`about`, `page`, `post`, `bib`, `cv`, `default`…).               |
| `_includes/`             | Reusable template snippets (header, footer, news list, social icons…).           |
| `_sass/`, `assets/css/`  | Styling. `_sass/_themes.scss` holds the color scheme if you want to recolor.     |
| `_plugins/`              | Custom Ruby plugins the theme relies on.                                         |
| `.github/workflows/deploy.yml` | Builds the site and pushes it to the `gh-pages` branch on every push to `main`/`master`. |
| `CNAME`                  | Custom domain (`benarmstrong.ca`). Don't delete.                                 |
| `_site/`, `.jekyll-cache/` | Build output / cache. Generated, git-ignored, safe to delete anytime.         |

### How deployment works

1. You push to `main`.
2. GitHub Actions (`deploy.yml`) runs `bundle exec jekyll build` in production mode, purges unused CSS, and pushes the built `_site/` to the `gh-pages` branch.
3. GitHub Pages serves the `gh-pages` branch at `benarmstrong.ca`.

Check the repo's **Actions** tab if a change doesn't appear — a failed build means nothing is published. Builds take a few minutes.

---

## Part 2 — Practical Jekyll commands

### One-time setup (macOS)

```bash
# Ruby: use a version manager rather than the system Ruby. CI uses Ruby 3.2.2.
brew install rbenv ruby-build imagemagick
rbenv install 3.2.2
rbenv local 3.2.2

# From the repo root, install the gems listed in Gemfile:
gem install bundler
bundle install
```

ImageMagick is required because `imagemagick.enabled: true` in `_config.yml`. If a gem fails to install, run `bundle update` and try again.

### Day-to-day commands

| Command | What it does |
| --- | --- |
| `bundle exec jekyll serve` | Build and serve at <http://localhost:4000>. Rebuilds when you save files (except `_config.yml`). |
| `bundle exec jekyll serve --livereload` | Same, and the browser refreshes automatically on save. |
| `bundle exec jekyll serve --future` | Also show items with future dates (useful to preview an upcoming news item). |
| `bundle exec jekyll build` | Build once into `_site/` without serving. Good for checking for errors. |
| `JEKYLL_ENV=production bundle exec jekyll build` | Build exactly the way the deploy action does. |
| `bundle exec jekyll clean` | Delete `_site/` and caches. Do this first if something looks stale or weird. |
| `bundle exec jekyll doctor` | Reports problems like two files writing to the same URL. |
| `Ctrl+C` | Stop the local server. |

Always prefix with `bundle exec` so you use the gem versions pinned for this project.

### Alternative: Docker

If Ruby setup is a pain, `docker compose up` (from the repo root) runs the site with everything preinstalled, served at <http://localhost:8080>. Requires Docker Desktop.

### Practical tips

- **Restart after editing `_config.yml`.** It's only read at startup.
- **Read the terminal output.** Liquid errors, BibTeX parse errors, and "Conflict: destination … is being written by multiple files" warnings appear there and explain most problems.
- **YAML front matter is whitespace-sensitive.** Use spaces (not tabs), put a space after each colon, and wrap values containing `:` or `#` in quotes.
- **Use `relative_url` / root-relative links.** In Markdown, link internal pages as `/publications/` or `{{ '/publications/' | relative_url }}` rather than hard-coding `https://benarmstrong.ca/...`.
- **Files and folders starting with `_` or `.` are not published** (unless listed under `include:` in `_config.yml`). Other files are copied to the site as-is, which is why stray Markdown files at the root should go in the `exclude:` list.
- **Check before pushing.** A quick local `bundle exec jekyll build` that finishes without errors is a good sign the deploy action will succeed.
- **Checking links locally:** after building, you can run a link checker over `_site/`, e.g. `gem install html-proofer && htmlproofer ./_site --disable-external` (drop `--disable-external` to also check external links; slower).
