# Changelog

## Unreleased

## 1.7.0 - 2026-07-05

+ [Removed] Removed registration feature; anti-abuse mechanism caused GitHub account bans.

## 1.6.0 - 2026-07-04

+ [Fixed] Fixed sub2api import issue.
+ [Fixed] Fixed frontend 404 and 405 errors.
+ [Added] Added conversation deletion after image generation.
+ [Changed] Pro accounts are no longer treated as unlimited; roughly 1,000 images per day.

## 1.5.0 - 2026-06-13

+ [Added] Added WARP / Privoxy / FlareSolverr bypass options; refreshes clearance and retries when Cloudflare blocks registration.
+ [Added] Added `outlook_token` email pool with Outlook/Hotmail registration code reading.
+ [Added] Added web search compatible endpoint, image editing mask, and image task capabilities.
+ [Improved] Updated sentinel/PoW acquisition to improve upstream request compatibility.
+ [Improved] Adjusted proxy priority and registration request retry logic.

## 1.4.1 - 2026-06-03

+ [Added] Account refresh is now asynchronous; frontend can poll refresh / re-login progress.
+ [Added] Added re-login to account pool page; supports password login to recover abnormal accounts.
+ [Added] Auto re-login abnormal accounts after refresh (can be enabled on the settings page).
+ [Added] Image generation supports parallel mode; multiple images use independent threads and accounts.
+ [Added] Image polling timeout auto-switches accounts and retries (up to 4 times); connection timeouts back off per account.
+ [Added] Image double-check mechanism and check-before-hit are now configurable; when disabled results return immediately.
+ [Added] Image task progress tracking shows current generation step (upload / warmup / token / generating).
+ [Added] Added "Continue waiting" button after image generation timeout.
+ [Added] Added image double-check, timeout wait, and auto re-login settings on the settings page.
+ [Improved] Improved image generation page scroll performance with lazy loading and saved/restored scroll position across conversations.

## 1.4.0 - 2026-05-31

+ [Added] Added AI-generated editable PSD file reverse engineering.
+ [Added] Added AI-generated editable PPT file reverse engineering.

## 1.3.1 - 2026-05-30

+ [Added] Added ChatGPT search debugging and Skills.

## 1.3.0 - 2026-05-30

+ [Added] Added ChatGPT search endpoint reverse engineering.

## 1.2.4 - 2026-05-30

+ [Added] Added chat completion caching and duplicate request merging.
+ [Added] Added infinite canvas one-click jump.

## 1.2.3 - 2026-05-29

+ [Added] Added account-level proxy.
+ [Fixed] Fixed 503 error message and frontend email line break issue.

## 1.2.2 - 2026-05-29

+ [Added] Added Codex image generation with 2k/4k support.
+ [Added] Added RT account info refresh.

## 1.2.0 - 2026-05-28

+ [Added] Baseline for current version, including web dashboard, image generation, account pool, registration, image manager, log manager, and settings.
+ [Added] Frontend version number supports click-to-open release modal showing current version, latest version, and changelog.
+ [Improved] Improved registration efficiency and success rate significantly.
+ [Improved] Improved image generation page configuration options.
