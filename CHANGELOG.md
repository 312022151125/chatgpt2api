# Changelog

## Unreleased

## 1.8.0 - 2026-07-28

+ [新增] 新增默认请求上游模型名称和默认思考强度配置，支持在设置页面修改，并可通过模型名的 `-standard`、`-extended`、`-max` 后缀覆盖思考强度。
+ [修复] 新增没出图也移除本地对话的配置，支持在图片生成失败、超时或仅返回文本时异步隐藏对应对话记录。
+ [修复] `/v1/models` 汇总各账号类型的官方模型列表，文本请求按模型权限选择账号。
+ [修复] 过滤隐藏、非最终频道及发往内部工具的助手消息，避免搜索指令和推理内容泄漏到 API 输出。
+ [修复] 修复输出清洗误删代码和命令中标点前空格的问题。
+ [修复] 为图片生成 SSE 流增加可配置的硬超时上限，避免上游长连接长时间挂起。
+ [优化] 数据库存储改为增量同步，仅新增、更新或删除发生变化的记录，保留未变记录的 ID。

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
