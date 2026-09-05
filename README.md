# zeroasterisk.com

Alan Blount's professional website - AI/ML Engineer at Google.

[![Deploy](https://github.com/zeroasterisk/zeroasterisk.com/actions/workflows/deploy.yml/badge.svg)](https://github.com/zeroasterisk/zeroasterisk.com/actions/workflows/deploy.yml)

## Overview

This site contains:
- **347 blog posts** spanning 2005-2026
- **Tech content** (AI/ML, development, infrastructure)
- **Personal stories** (travel, family, life experiences)
- **Cross-posts** from Google publications
- **Year-based tagging** for temporal organization

## Technology Stack

- **Framework**: Hugo (v0.121.1)
- **Theme**: Custom minimal-tech theme
- **Hosting**: GitHub Pages
- **CI/CD**: GitHub Actions
- **Domain**: zeroasterisk.com

## Development

### Local Development

```bash
# Clone the repository
git clone https://github.com/zeroasterisk/zeroasterisk.com.git
cd zeroasterisk.com

# Install Hugo
# See: https://gohugo.io/installation/

# Run local development server
hugo server -D --bind 0.0.0.0 --baseURL http://localhost:1313

# Visit: http://localhost:1313
```

### Content Structure

```
content/
├── posts/          # Technical content (180 posts)
├── personal/       # Personal stories (167 posts)
└── pages/          # Static pages (about, etc.)
```

### Theme Customization

The custom `minimal-tech` theme provides:
- **Graph paper background** with coffee stain effects
- **Engineering typography** (Courier New, Monaco)
- **Unified button styling** across navigation and tags
- **Cross-post indicators** for external publications
- **Responsive design** for all screen sizes

## Deployment

### Production Deployment

1. **Create Pull Request**: All changes go through PR review
2. **CI Testing**: Automated Hugo build verification  
3. **Merge to Main**: Triggers production deployment
4. **GitHub Pages**: Automatic deployment to zeroasterisk.com
5. **Verification**: Automated URL testing post-deployment

### Branch Protection

- **No direct commits** to `main` branch
- **PR review required** before merge
- **CI checks must pass** before merge allowed
- **Auto-delete feature branches** after merge

### CI/CD Pipeline

The `.github/workflows/deploy.yml` handles:

```yaml
on:push:main → build → deploy → verify
on:pull_request → test-build (no deploy)
```

## Content Migration

All content was migrated from two original Hugo sites:
- `hugo-zeroasterisk.com` (339 posts)  
- `hugo-code.zeroasterisk.com` (9 posts)

Migration included:
- ✅ **Smart categorization** (tech vs personal)
- ✅ **Year tags** for temporal organization  
- ✅ **URL preservation** for SEO compliance
- ✅ **Frontmatter normalization** 
- ✅ **Cross-post attribution** for external content

## URL Structure

### Legacy URL Compatibility

All original URLs are preserved:
- `/YYYY/MM/post-title/` (tech posts)
- `/personal/YYYY/MM/post-title/` (personal posts)

### Navigation URLs

- `/` - Homepage with recent posts
- `/posts/` - All tech content  
- `/personal/` - All personal stories
- `/about/` - About Alan Blount
- `/tags/` - Tag cloud and organization
- `/search/` - Site search

### Feeds & Meta

- `/sitemap.xml` - Complete site map
- `/index.xml` - Main RSS feed
- `/posts/index.xml` - Tech posts RSS
- `/personal/index.xml` - Personal RSS

## Content Guidelines

### Cross-Posting Pattern

For external publications (Google blogs, papers, etc.):

1. **Brief Summary**: 2-3 sentence overview
2. **Canonical Link**: Clear attribution to original
3. **Visual Indicator**: Blue border and badge
4. **SEO Tags**: `cross-post` + relevant topic tags

See `CROSSPOST_PATTERN.md` for full workflow.

### Tagging Strategy

- **Topic tags**: elixir, ai, meteor, development
- **Year tags**: 2005, 2006, ..., 2026  
- **Category tags**: tech, personal
- **Special tags**: cross-post, google, conference

## Analytics & Monitoring

- **GitHub Pages**: Built-in hosting analytics
- **GitHub Actions**: CI/CD pipeline monitoring
- **URL Verification**: Automated testing post-deployment

## Contributing

1. **Fork** the repository
2. **Create feature branch**: `git checkout -b feat/description`
3. **Make changes** using proper commit messages
4. **Push branch**: `git push origin feat/description`  
5. **Open Pull Request** with description
6. **Wait for CI** and code review
7. **Merge** when approved and green

## Contact

- **Website**: https://zeroasterisk.com
- **LinkedIn**: https://linkedin.com/in/alanblount
- **Twitter**: https://twitter.com/zeroasterisk  
- **GitHub**: https://github.com/zeroasterisk

---

**Built with ❤️ and ☕ in Boulder, Colorado**
<!-- Production deployment Sat Sep  5 02:45:25 UTC 2026 -->

<!-- CNAME trigger Sat Sep  5 02:51:28 UTC 2026 -->
