# Graph Report - .  (2026-07-21)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 2178 nodes · 5599 edges · 103 communities (81 shown, 22 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 143 edges (avg confidence: 0.53)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `71be0071`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9
- Community 10
- Community 11
- Community 12
- Community 13
- Community 14
- Community 15
- Community 16
- Community 17
- Community 18
- Community 19
- Community 20
- Community 21
- Community 22
- Community 23
- Community 24
- Community 25
- Community 26
- Community 27
- Community 28
- Community 29
- Community 30
- Community 31
- Community 32
- Community 33
- Community 34
- Community 35
- Community 36
- Community 37
- Community 38
- Community 39
- Community 40
- Community 41
- Community 42
- Community 43
- Community 44
- Community 45
- Community 46
- Community 47
- Community 48
- Community 49
- Community 50
- Community 51
- Community 52
- Community 53
- Community 54
- Community 55
- Community 56
- Community 57
- Community 58
- Community 59
- Community 60
- Community 61
- Community 62
- Community 63
- Community 64
- Community 65
- Community 66
- Community 67
- Community 68
- Community 69
- Community 70
- Community 71
- Community 72
- Community 73
- Community 74
- Community 75
- Community 76
- Community 77
- Community 78
- Community 79
- Community 80
- Community 81
- Community 82
- Community 83
- Community 84
- Community 85
- Community 86
- Community 87
- Community 88
- Community 89
- Community 90
- Community 91
- Community 92
- Community 93
- Community 94
- Community 95
- Community 96
- Community 97
- Community 98
- Community 99

## God Nodes (most connected - your core abstractions)
1. `OpenAIBackendAPI` - 143 edges
2. `AccountService` - 100 edges
3. `cn()` - 93 edges
4. `httpRequest()` - 68 edges
5. `ConfigStore` - 44 edges
6. `ImagePageContent()` - 33 edges
7. `ProxySettingsStore` - 31 edges
8. `Button()` - 30 edges
9. `AuthService` - 28 edges
10. `StorageBackend` - 28 edges

## Surprising Connections (you probably didn't know these)
- `filter_or_log()` --indirect_call--> `check_request()`  [INFERRED]
  api/ai.py → services/content_filter.py
- `ImageGenerationTaskRequest` --uses--> `LoggedCall`  [INFERRED]
  api/image_tasks.py → services/log_service.py
- `ResumePollRequest` --uses--> `LoggedCall`  [INFERRED]
  api/image_tasks.py → services/log_service.py
- `AccountExportTests` --uses--> `AccountService`  [INFERRED]
  test/test_account_export.py → services/account_service.py
- `MemoryStorage` --uses--> `AccountService`  [INFERRED]
  test/test_account_export.py → services/account_service.py

## Import Cycles
- None detected.

## Communities (103 total, 22 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (70): BackupDeleteRequest, ClearanceTestRequest, create_router(), ImageDeleteRequest, ImageDownloadRequest, ImageTagsRequest, LogDeleteRequest, ProxyTestRequest (+62 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (77): ProxySettingsCard(), AuthMode, normalizeAccounts(), PAGE_SIZE_OPTIONS, Sub2APIConnections(), DEFAULT_PROXY_RUNTIME, DEFAULT_THIRD_PARTY_APPS, normalizeConfig() (+69 more)

### Community 2 - "Community 2"
Cohesion: 0.07
Nodes (28): FlareSolverrRequestMethod, Lock, _clean(), ClearanceBundle, _coerce_timeout(), _colon_proxy_to_url(), _cookies_to_header(), _domain_matches() (+20 more)

### Community 3 - "Community 3"
Cohesion: 0.06
Nodes (24): ConfigStore, _is_invalid_auth_key(), _load_settings(), LoadedSettings, _normalize_auth_key(), _normalize_backup_include(), _normalize_backup_settings(), _normalize_bool() (+16 more)

### Community 4 - "Community 4"
Cohesion: 0.08
Nodes (23): ABC, Base, Repo, export_to_json(), import_from_json(), main(), migrate_data(), test_storage() (+15 more)

### Community 5 - "Community 5"
Cohesion: 0.09
Nodes (54): ImageContentPolicyError, ImagePollTimeoutError, Raised when image generation is blocked by content policy moderation., add_unique(), apply_patch_op(), apply_text_patch(), assistant_history_messages(), assistant_history_text() (+46 more)

### Community 6 - "Community 6"
Cohesion: 0.12
Nodes (37): ChatPanel(), messageImages(), messageText(), readImage(), SelectedImage, pretty(), aspectOptions, countOptions (+29 more)

### Community 7 - "Community 7"
Cohesion: 0.11
Nodes (15): _clean(), _image_dimensions(), ImageStorageService, _is_image_rel(), _local_image_path(), _now_iso(), Path, _read_json_object() (+7 more)

### Community 8 - "Community 8"
Cohesion: 0.08
Nodes (19): main(), main(), main(), main(), ImageEditsTests, load_asset_bytes(), summarize_chunk(), ImageGenerationsTests (+11 more)

### Community 9 - "Community 9"
Cohesion: 0.09
Nodes (31): _compatible_error_response(), install_exception_handlers(), _is_anthropic_messages_path(), FastAPI, JSONResponse, Request, _collect_account_emails(), _collect_conversation_ids() (+23 more)

### Community 10 - "Community 10"
Cohesion: 0.08
Nodes (4): AccountService, datetime, Path, 账号池服务，使用 token -> account 的 dict 保存账号。

### Community 11 - "Community 11"
Cohesion: 0.08
Nodes (37): HeaderActions(), ThemeToggle(), adminNavItems, buildThirdPartyHref(), TopNav(), userNavItems, AnimatedThemeToggler(), AnimatedThemeTogglerProps (+29 more)

### Community 12 - "Community 12"
Cohesion: 0.10
Nodes (30): BackupSettingsCard(), formatBytes(), formatDateTime(), getFilenameFromContentDisposition(), includeLabels, formatDateTime(), UserKeysCard(), Badge() (+22 more)

### Community 13 - "Community 13"
Cohesion: 0.12
Nodes (27): SkillPanel(), LoginPage(), HomePage(), ApiDoc, ApiDocsCard(), docs, ParamRow, usableModels (+19 more)

### Community 14 - "Community 14"
Cohesion: 0.16
Nodes (34): encode_images(), text_backend(), chat_completion_annotations(), chat_image_args(), chat_messages_from_body(), completion_chunk(), completion_response(), handle() (+26 more)

### Community 15 - "Community 15"
Cohesion: 0.16
Nodes (15): _clean(), _collect_image_urls(), ImageTaskService, _now_iso(), _owner_id(), _public_task(), Any, Path (+7 more)

### Community 16 - "Community 16"
Cohesion: 0.13
Nodes (29): collect_image_outputs(), stream_image_chunks(), _composite_mask(), handle(), Any, 将 mask 的 alpha 通道合成到图片中，标识需要编辑的区域。          mask 的透明区域（低 alpha）= 需要编辑的区域，     ma, handle(), Any (+21 more)

### Community 17 - "Community 17"
Cohesion: 0.13
Nodes (15): ChatRequirements, Response, RuntimeError, 获取当前模式对话所需的 sentinel token（prepare + finalize 两步流程）。, 根据当前 requirements 构造对话 SSE 请求头。, 把标准 chat messages 转成 web conversation 所需的 messages。, 保存一次对话请求所需的 sentinel token。, 把标准 messages 构造成 web 对话请求体。 (+7 more)

### Community 18 - "Community 18"
Cohesion: 0.10
Nodes (6): OpenAIBackendAPI, ChatGPT Web 后端封装。      说明：     - 传入 `access_token` 时，聊天和模型列表都会走已登录链路       例如 `/, 初始化后端客户端。          参数：         - `access_token`：可选。传入后表示使用已登录链路；不传则使用未登录链路。, Report progress step to the callback if set., handle(), main()

### Community 19 - "Community 19"
Cohesion: 0.10
Nodes (7): Any, 获取完整 conversation 详情。, 列出最近的对话列表，按更新时间倒序。          当 SSE 流太短导致 conversation_id 丢失时，可以通过此方法         查找最近, 根据 prompt 和开始时间，从最近对话列表中查找匹配的 conversation_id。          当 SSE 流太短导致 conversation, 从 conversation 明细里提取图片工具输出记录。, 构造请求头，并补上 web 端要求的 target path/route。, 返回当前模式下可用模型，格式对齐 OpenAI `/v1/models`。

### Community 20 - "Community 20"
Cohesion: 0.19
Nodes (31): count_message_image_tokens(), count_message_text_tokens(), count_text_tokens(), encoding_for_model(), _append_response_message(), collect_response(), extract_response_image(), handle() (+23 more)

### Community 21 - "Community 21"
Cohesion: 0.06
Nodes (31): axios, class-variance-authority, clsx, date-fns, localforage, motion, @radix-ui/react-dialog, @radix-ui/react-popover (+23 more)

### Community 22 - "Community 22"
Cohesion: 0.16
Nodes (5): Any, 返回所有账号的副本，并为每个账号附加当前图片在途数 image_inflight。          image_inflight 为内存态并发计数(账号正在生, 更新单个重新登录进度。当所有账号处理完毕时自动标记完成。, 对选中账号执行密码重新登录流程。          仅对包含 email + password 的账号有效。         登录成功后自动将状态设为"正常"。, anonymize_token()

### Community 23 - "Community 23"
Cohesion: 0.07
Nodes (29): eslint, eslint-config-next, eslint-config-prettier, @eslint/eslintrc, prettier-plugin-organize-imports, prettier-plugin-tailwindcss, tailwindcss, @tailwindcss/postcss (+21 more)

### Community 24 - "Community 24"
Cohesion: 0.14
Nodes (5): Pattern, EditableFileArtifact, EditableFileExportResult, Path, 把 base64 图片字符串或本地路径解码成二进制。

### Community 25 - "Community 25"
Cohesion: 0.07
Nodes (28): dom, dom.iterable, esnext, next.config.ts, .next/dev/types/**/*.ts, next-env.d.ts, .next/types/**/*.ts, node_modules (+20 more)

### Community 26 - "Community 26"
Cohesion: 0.14
Nodes (7): InvalidAccessTokenError, JSONStorageBackend, Any, Path, AccountCapabilityTests, AuthServiceTests, TokenLogTests

### Community 28 - "Community 28"
Cohesion: 0.13
Nodes (27): ImageSidebar(), ImageSidebarProps, ImageModel, clearImageConversations(), dataUrlMimeType(), deleteImageConversation(), getImageConversationStats(), getLegacyReferenceImages() (+19 more)

### Community 29 - "Community 29"
Cohesion: 0.15
Nodes (25): _account_payload_token(), _account_zip_bytes(), AccountCreateRequest, AccountDeleteRequest, AccountExportRequest, AccountRefreshRequest, AccountUpdateRequest, CPAImportRequest (+17 more)

### Community 30 - "Community 30"
Cohesion: 0.11
Nodes (27): _clean(), _decode_data_url(), _download_image_url(), _extension_from_mime(), _filename_from_url(), _is_upload(), _parse_bool(), _parse_count() (+19 more)

### Community 31 - "Community 31"
Cohesion: 0.14
Nodes (26): activeConversationQueueIds, buildConversationTitle(), buildReferenceImageFromResult(), buildReferenceImageFromStoredImage(), clampImageCount(), createId(), dataUrlToFile(), fetchImageAsFile() (+18 more)

### Community 32 - "Community 32"
Cohesion: 0.15
Nodes (11): CPAConfig, CPAImportService, fetch_remote_access_token(), list_remote_files(), _management_headers(), _new_id(), _normalize_import_job(), _normalize_pool() (+3 more)

### Community 33 - "Community 33"
Cohesion: 0.15
Nodes (26): build_tool_prompt(), _compact_message_text(), compact_system(), _compact_system_text(), content_blocks(), handle(), _has_claude_code_system(), merge_system() (+18 more)

### Community 34 - "Community 34"
Cohesion: 0.12
Nodes (19): AccountsPage(), PptPanel(), PsdPanel(), DebugPage(), tabs, ImageManagerPage(), ImagePage(), LogsPage() (+11 more)

### Community 35 - "Community 35"
Cohesion: 0.14
Nodes (21): formatSize(), imageKey(), ImageManagerContent(), DateRangeFilter(), DateRangeFilterProps, Calendar(), Popover(), PopoverContent() (+13 more)

### Community 36 - "Community 36"
Cohesion: 0.21
Nodes (12): request_text(), _clean(), _editable_access_token(), EditableFileTaskService, _elapsed_seconds(), _file_url(), _now_iso(), _owner_id() (+4 more)

### Community 37 - "Community 37"
Cohesion: 0.14
Nodes (24): AccountsPageContent(), accountStatusOptions, displayAccountSource(), displayAccountType(), downloadTokens(), formatCompact(), formatQuota(), formatQuotaSummary() (+16 more)

### Community 38 - "Community 38"
Cohesion: 0.18
Nodes (22): createClientTaskId(), EditableFilePanel(), fileNameOf(), formatElapsed(), isRunning(), mergeTasks(), Props, readFile() (+14 more)

### Community 39 - "Community 39"
Cohesion: 0.19
Nodes (21): ArgumentParser, Message, build_parser(), _clean(), _decode_header(), exchange_refresh_token(), _graph_sender(), _http_request() (+13 more)

### Community 40 - "Community 40"
Cohesion: 0.26
Nodes (4): AuthRole, AuthService, _hash_key(), _now_iso()

### Community 41 - "Community 41"
Cohesion: 0.14
Nodes (15): HTMLParser, 把 sentinel 响应整理成后续对话需要的 token 集合。, build_legacy_requirements_token(), build_pow_config(), build_proof_token(), _legacy_parse_time(), parse_pow_resources(), _pow_generate() (+7 more)

### Community 42 - "Community 42"
Cohesion: 0.14
Nodes (18): create_app(), FastAPI, create_router(), APIRouter, extract_bearer_token(), _legacy_admin_identity(), Event, Exception (+10 more)

### Community 43 - "Community 43"
Cohesion: 0.13
Nodes (5): FakeAccountService, FakeConfig, FakeProxySettings, FakeStorage, ProxyRuntimeApiTests

### Community 44 - "Community 44"
Cohesion: 0.10
Nodes (19): aliases, components, hooks, lib, ui, utils, iconLibrary, registries (+11 more)

### Community 45 - "Community 45"
Cohesion: 0.22
Nodes (17): _auth_headers(), _clean(), _extract_access_token(), _extract_paged_items(), _fetch_access_tokens_for_accounts(), list_remote_accounts(), list_remote_groups(), _login() (+9 more)

### Community 46 - "Community 46"
Cohesion: 0.14
Nodes (9): OAuthLoginService, 手动 OAuth 桥服务  让用户用自己浏览器走一遍 OpenAI 的标准 OAuth + PKCE 授权码流程：   1. 后端生成 code_verifie, 从 callback URL 或 raw code 中提取 (code, state)。          既允许用户粘贴整段 platform.openai., 用 session_id 配对的 code_verifier 把 callback 里的 code 换成 token 三件套。          - 优先用 c, 调用 /api/accounts/oauth/token 用 code+verifier 换 token 三件套。, 维护 PKCE 临时会话，并完成 code → token 的兑换。, 生成 PKCE code_verifier 与对应的 code_challenge（S256）。, 清理过期或溢出容量的会话，必须在持锁状态下调用。 (+1 more)

### Community 47 - "Community 47"
Cohesion: 0.25
Nodes (9): cache_key(), CacheEntry, canonical_body(), ChatCompletionCache, InflightCall, _json_safe(), _message_signature(), normalize_text_messages() (+1 more)

### Community 48 - "Community 48"
Cohesion: 0.16
Nodes (17): b64BlobUrlCache, base64SizeCache, downloadStoredImage(), formatBase64ImageSize(), formatDuration(), formatElapsed(), formatImageDimensions(), getProgressLabel() (+9 more)

### Community 49 - "Community 49"
Cohesion: 0.18
Nodes (14): filter_or_log(), ImageGenerationTaskRequest, BaseModel, ResumePollRequest, check_request(), _extract_review_decision(), _is_allow_decision(), _is_reject_decision() (+6 more)

### Community 50 - "Community 50"
Cohesion: 0.19
Nodes (4): ImageOutput, _conversation(), FakeBackend, MultiImageResultTests

### Community 51 - "Community 51"
Cohesion: 0.23
Nodes (15): _decode_base64_image(), _json_image_sources(), _json_mask_sources(), _json_reference_value(), parse_image_edit_request(), Any, Request, 提取图片引用对象：支持 image_url 或 url，明确拒绝 file_id。 (+7 more)

### Community 52 - "Community 52"
Cohesion: 0.13
Nodes (6): _is_content_policy_error(), 从对话文档中查找内容政策违规错误消息。          上游拒绝生成图片时，错误消息会出现在 assistant 消息的文本中。         本方法遍历所, Poll the conversation document until image file ids appear or budget runs out., 通过 conversation 附件接口获取下载地址。, 查询 /backend-api/tasks/ 接口获取异步任务状态和错误信息。          参数：         - `conversation_id`, 检查单个任务是否包含结构化错误。          通过以下字段判断（不依赖文本匹配）：         - image_gen_message.metadat

### Community 53 - "Community 53"
Cohesion: 0.25
Nodes (4): AccountExportTests, make_jwt(), MemoryStorage, Any

### Community 54 - "Community 54"
Cohesion: 0.19
Nodes (13): AccountImportDialog(), AccountImportDialogProps, getAccountJsonAccount(), getAccountJsonAccounts(), getCodexAuthAccount(), getSessionAccessToken(), ImportMethod, PendingAccountJsonImport (+5 more)

### Community 55 - "Community 55"
Cohesion: 0.23
Nodes (13): formatDuration(), getDetailText(), getStatus(), getUrls(), LogsContent(), LogType, typeLabels, getImageThumbnailUrl() (+5 more)

### Community 56 - "Community 56"
Cohesion: 0.30
Nodes (13): AnthropicMessageRequest, ChatCompletionRequest, create_router(), EditableFileTaskRequest, filter_or_log(), ImageGenerationRequest, APIRouter, BaseModel (+5 more)

### Community 57 - "Community 57"
Cohesion: 0.16
Nodes (13): react, react, CharBox, CharBoxProps, CONTAINER_TRANSFORMS, DEFAULT_TRANSITION, extractTextFromChildren(), FRONT_FACE_TRANSFORMS (+5 more)

### Community 59 - "Community 59"
Cohesion: 0.26
Nodes (4): _new_id(), _normalize_server(), Path, Sub2APIConfig

### Community 60 - "Community 60"
Cohesion: 0.17
Nodes (3): FakeImageTaskService, ImageTasksApiTests, 测试图片编辑任务接口支持表单 image_url 引用。

### Community 61 - "Community 61"
Cohesion: 0.32
Nodes (11): _decode_json_image_string(), _decode_message_image_object(), _decode_message_image_url(), extract_chat_image(), extract_chat_prompt(), extract_image_from_message_content(), _extract_json_image_value(), extract_prompt_from_message_content() (+3 more)

### Community 62 - "Community 62"
Cohesion: 0.29
Nodes (5): build_sentinel_token(), OpenAI Sentinel Token (PoW) 生成与请求工具函数。  用于密码登录、注册等需要 sentinel token 的流程。, 请求 sentinel token 并返回 (sentinel_header_value, oai_sc_cookie_value)。      Args:, Sentinel Token 生成器（PoW - Proof of Work）。, SentinelTokenGenerator

### Community 63 - "Community 63"
Cohesion: 0.27
Nodes (8): nextConfig, projectRoot, isNewerVersion(), readLocalReleases(), toVersionParts(), useVersionCheck(), parseChangelog(), ReleaseInfo

### Community 64 - "Community 64"
Cohesion: 0.17
Nodes (11): name, overrides, @types/react, @types/react-dom, private, scripts, build, dev (+3 more)

### Community 65 - "Community 65"
Cohesion: 0.23
Nodes (10): cleanUrl(), MarkdownResult(), normalizeMarkdown(), SearchPanel(), sourceKind(), ChatCompletionResponse, ChatContentPart, ChatMessage (+2 more)

### Community 67 - "Community 67"
Cohesion: 0.27
Nodes (10): clamp(), getTouchCenter(), getTouchDistance(), ImageLightbox(), ImageLightboxProps, ImageTransform, LightboxImage, normalizeTransform() (+2 more)

### Community 68 - "Community 68"
Cohesion: 0.50
Nodes (8): _deep_fill_missing(), _env_bool(), _env_int(), _looks_like_repository_default(), main(), _mask_url(), Any, _warp_runtime_defaults()

### Community 69 - "Community 69"
Cohesion: 0.22
Nodes (3): list_models(), Any, ModelListTests

### Community 70 - "Community 70"
Cohesion: 0.36
Nodes (7): diagnose(), _fmt_remaining(), force_refresh(), main(), 验证 OAuth 账号的自动刷新是否生效。  用法（在容器内，工作目录 /app）：     uv run python scripts/verify_oaut, 只读：打印每个账号的刷新就绪状态，返回带 refresh_token 的 token 列表。, 对每个账号 force 刷新一次，并对比前后状态判断成败。

### Community 71 - "Community 71"
Cohesion: 0.32
Nodes (3): ChatCompletionsTests, Path, save_images_from_text()

### Community 73 - "Community 73"
Cohesion: 0.29
Nodes (3): ImagesEditsApiTests, 测试图片编辑接口支持官方 JSON image_url 引用。, 测试图片编辑接口对暂不支持的 file_id 返回明确错误。

### Community 74 - "Community 74"
Cohesion: 0.43
Nodes (6): buildGradient(), DEFAULT_COLORS, DiaTextReveal(), DiaTextRevealProps, measureWidths(), sweepEase()

### Community 75 - "Community 75"
Cohesion: 0.47
Nodes (6): create_router(), APIRouter, sanitize_cpa_pool(), sanitize_cpa_pools(), sanitize_sub2api_server(), sanitize_sub2api_servers()

### Community 76 - "Community 76"
Cohesion: 0.33
Nodes (4): 通过邮箱+密码登录，返回 {access_token, refresh_token, id_token, ...}, generate_pkce(), PKCE (Proof Key for Code Exchange) 工具函数, 生成 PKCE code_verifier 与对应的 code_challenge（S256）。      Returns:         (code_ver

### Community 80 - "Community 80"
Cohesion: 0.40
Nodes (3): metadata, viewport, ThemeScript()

### Community 81 - "Community 81"
Cohesion: 0.40
Nodes (4): MorphingText(), MorphingTextProps, Texts(), useMorphingText()

### Community 82 - "Community 82"
Cohesion: 0.40
Nodes (4): Any, RuntimeError, Raised when an upstream HTTP call returns a non-2xx status.      Carries structu, UpstreamHTTPError

### Community 83 - "Community 83"
Cohesion: 0.70
Nodes (5): deriveTurnStatus(), finalizeIdleQueuedTurn(), recoverConversationHistory(), syncConversationImageTasks(), saveImageConversations()

### Community 84 - "Community 84"
Cohesion: 0.83
Nodes (3): find_images(), main(), parse_events()

## Knowledge Gaps
- **173 isolated node(s):** `chatgpt2api`, `$schema`, `style`, `rsc`, `tsx` (+168 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **22 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `OpenAIBackendAPI` connect `Community 18` to `Community 33`, `Community 36`, `Community 5`, `Community 69`, `Community 41`, `Community 10`, `Community 14`, `Community 15`, `Community 17`, `Community 82`, `Community 19`, `Community 52`, `Community 50`, `Community 22`, `Community 24`, `Community 26`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Why does `AccountService` connect `Community 10` to `Community 58`, `Community 4`, `Community 76`, `Community 18`, `Community 53`, `Community 22`, `Community 26`?**
  _High betweenness centrality (0.065) - this node is a cross-community bridge._
- **Why does `ConfigStore` connect `Community 3` to `Community 4`?**
  _High betweenness centrality (0.046) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `OpenAIBackendAPI` (e.g. with `AccountService` and `EditableFileTaskService`) actually correct?**
  _`OpenAIBackendAPI` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `AccountService` (e.g. with `InvalidAccessTokenError` and `OpenAIBackendAPI`) actually correct?**
  _`AccountService` has 8 INFERRED edges - model-reasoned connections that need verification._
- **What connects `chatgpt2api`, `$schema`, `style` to the rest of the system?**
  _173 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.051748009691934924 - nodes in this community are weakly interconnected._