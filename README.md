# HUEO / 原画光年 Legal Pages

Static bilingual support and legal pages for **HUEO (原画光年)**.

## Pages

- `index.html` — product support and contact page
- `privacy/index.html` — Privacy Policy / 隐私政策
- `privacy/terms.html` — Terms of Use / 使用条款

The pages support English and Simplified Chinese. They select a language from `?lang=en` or
`?lang=zh-Hans`, then fall back to the browser language.

## Recommended GitHub Pages setup

1. Create a public repository named `autolut-legal` under the intended publisher account.
2. Push this directory to the repository's default branch.
3. In **Settings > Pages**, deploy from the default branch root.
4. Confirm every URL below is publicly accessible without signing in.

If the repository is published under `RobinCoderZhao/autolut-legal`, the intended URLs are:

- Support URL: `https://robincoderzhao.github.io/autolut-legal/`
- Privacy Policy URL: `https://robincoderzhao.github.io/autolut-legal/privacy/`
- Terms of Use URL: `https://robincoderzhao.github.io/autolut-legal/privacy/terms.html`

If the publisher account or repository name changes, update these URLs in App Store Connect and in
the App before release.

## App Store Connect mapping

- **Support URL**: the root support page
- **Privacy Policy URL**: the privacy page
- **App description / subscription metadata**: link to the Terms of Use where appropriate
- Keep Apple's Standard EULA as the licensed-application EULA unless a separately reviewed custom
  EULA is intentionally configured in App Store Connect.

## Release checklist

- Verify the contact email `414108176@qq.com` is monitored.
- Verify the product behavior and privacy disclosures still match the shipping build.
- Verify StoreKit product names, billing periods, prices, trials, and Family Sharing directly in
  App Store Connect; these pages intentionally do not hard-code prices or promise a trial.
- Re-review the pages whenever analytics, accounts, cloud storage, networking, permissions, export
  quota, or purchase behavior changes.

Effective date of the included policies: **August 21, 2026**.
