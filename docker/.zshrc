# 補完
autoload -Uz compinit && compinit
unsetopt correct

# 日本語対応
export LANG=ja_JP.UTF-8
setopt print_eight_bit

# エイリアス
alias ojt='oj t -c "python3 main.py"'

# プロンプト
PROMPT='%F{cyan}%~ %f
> '