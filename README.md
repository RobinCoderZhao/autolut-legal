# HUEO / 原画光年 Legal Pages

Static bilingual support and legal pages for **HUEO (原画光年)**.

## Pages

- `index.html` — product support and contact page
- `privacy/index.html` — Privacy Policy / 隐私政策
- `privacy/terms.html` — Terms of Use / 使用条款

The pages support English and Simplified Chinese. They select a language from `?lang=en` or
`?lang=zh-Hans`, then fall back to the browser language.

## Publishing

This repository publishes through `.github/workflows/deploy-pages.yml` on pushes to `main`
or a manual workflow dispatch. The workflow uploads the repository root and deploys it to GitHub Pages.
After a release update, verify that the workflow succeeds and all three public pages show
the new content in both languages.

Public URLs:

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

Revision date of the included policies: **October 2, 2026**. The revisions take effect when
published, subject to any notice or consent required by section 17 of the Terms and applicable law.
Commit locally first, then push when the App update is ready: a local commit does not publish
the site, while pushing `main` triggers the existing Pages workflow.

## Current content baseline

The App Album additions were checked against AutoLUT/HUEO source commit
`28f7a2539f9df8324e01bbda0ccaf6fbbf5a0616`. Existing disclosures for external-device import,
Photos video selection, local diagnostics, capture metadata, and Settings-only recommendations
are retained. Feature descriptions apply to App versions that include those features; this
baseline does not mean the new App version or these revised pages have already been published.

Implementation evidence in the AutoLUT repository:

- `PlatformClients/OriginalMediaImporter.swift` and `PhotoKitLivePhotoVideoLibrary.swift` — Photos read access and video selection.
- `PlatformClients/ExternalMediaImportRuntime.swift`, `ExternalMediaPhotoLibraryClient.swift`, and `LivePhotoPhotoLibraryClient.swift` — external import, Photos add access, and capture metadata.
- `PlatformClients/AppDiagnosticPersistence.swift`, `MetricKitPayloadRedactor.swift`, and `AppDiagnosticPackageExporter.swift` — diagnostic content, retention, redaction, sharing, and cleanup.
- `AutoLUTFeatures/OtherAppsCatalog.swift` and `OtherAppsView.swift` — bundled recommendations and plain App Store links.
- `AppContracts/AppPhotoAlbumClient.swift` and `PlatformClients/PhotoKitAppAlbumOrganizer.swift` — full-access-only album membership changes, local album-identifier caching, a bounded in-memory queue, and failure isolation.
- `AutoLUTFeatures/AppPhotoAlbumSettingsView.swift` — explicit authorization and current permission/status display.
- `Apps/Shared/AppEnvironment.swift`, `AutoLUTFeatures/ApplicationClients.swift`, `AutoLUTFeatures/AppFeature.swift`, and `PlatformClients/ExternalMediaImportRuntime.swift` — organization after confirmed save records for Live Photos, Photos color exports, and external imports.
- `assets/site.js` and `.github/workflows/deploy-pages.yml` in this repository — language selection and GitHub Pages hosting; the Privacy Policy identifies the hosting provider's ordinary website requests separately from App processing.

Module paths above are relative to `Packages/AutoLUTKit/Sources/`; `Apps/Shared/` paths are
relative to the application repository root. Product/permission behavior
must be checked against code rather than copied from an older policy. This update changes
feature and data-handling descriptions; existing prices, allowance, subscription, refund,
and liability terms are unchanged.
