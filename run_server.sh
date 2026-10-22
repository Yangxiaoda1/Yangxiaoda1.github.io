#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

export no_proxy="${no_proxy:+${no_proxy},}127.0.0.1,localhost"
export NO_PROXY="${NO_PROXY:+${NO_PROXY},}127.0.0.1,localhost"

if ! command -v ruby >/dev/null || ! command -v bundle >/dev/null; then
  echo "缺少 Ruby 或 Bundler，请参阅 LOCAL_DEVELOPMENT.md。" >&2
  exit 1
fi
if ! bundle check > /dev/null 2>&1; then
  echo "正在安装 Gemfile.lock 中的依赖……"
  bundle install
fi

# 网络共享目录可能不发送文件变化事件，因此本地开发默认使用轮询。
exec bundle exec jekyll serve \
  --host "${HOST:-127.0.0.1}" \
  --port "${PORT:-4000}" \
  --livereload \
  --livereload-port "${LIVERELOAD_PORT:-35729}" \
  --force_polling "$@"
