" REFERENCE DOCS
" ==============
" A set of vim, zsh, git, and tmux configuration files.
" https://thoughtbot.com/open-source
"
" Really good articles on how to use vim
" https://robots.thoughtbot.com/tags/vim


" COMMAND HELP
" ============
" vip: visial select paragraph
" v:   visual mode used to select text
" gq:  rewrap text block
"
"
" SPELLING HELP
" =============
" set spell             " Enable spell checking
" set nospell           " Disable spell checking
" <CTRL>+N or <CTRL>+P  " Word completion
" zg                    " Add word to dictionary (good word)
" ]s                    " Move to previous misspelled word
" [s                    " Move to next misspelled word
" z=                    " Word suggestion
"
" textwidth (or tw):
"     controls the wrap width you would like to use. Use :se tw=72 to set
"     the wrap width; by default it's unset and thus disables line-wrapping.
"     If this value is set, you're entirely at the whimsy of the below 
"     formatoptions, which is often filetype sensitive.
"
" formatoptions (or fo):
"     Controls whether or not automatic text wrapping is enabled, depending on
"     whether or not the t flag is set. Toggle the flag on with :set fo+=t,
"     and toggle it off with :set fo-=t. There are also a number of auxiliary
"     format options, but they're not as important.  wrapmargin (or wm):
"     controls when to wrap based on terminal size; I generally find using
"     this to be a bad idea.
"
" Example wrapping configurations:
"
"     No automatic wrapping, rewrapping will wrap to 72
"         textwidth=72 formatoptions=cq wrapmargin=0
"
"     No automatic wrapping, rewrapping will wrap to 72
"         textwidth=0 formatoptions=cqt wrapmargin=0
"
"     No automatic wrapping, rewrapping will wrap to 80
"         textwidth=0 formatoptions=cq wrapmargin=0
"
"     Automatic wrapping at a 5 col right margin
"         textwidth=0 formatoptions=cqt wrapmargin=5
"
"     Automatic wrapping at col 72
"         textwidth=72 formatoptions=cqt wrapmargin=0

" execute pathogen#infect()

" Leader
let mapleader = " "

set sessionoptions-=options
set nocompatible
set viminfo=

set backspace=2   " Backspace deletes like most programs in insert mode
set nobackup
set nowritebackup
set noswapfile    " http://robots.thoughtbot.com/post/18739402579/global-gitignore#comment-458413287
set history=50
set ruler         " show the cursor position all the time
set showcmd       " display incomplete commands
set incsearch     " do incremental searching
set laststatus=2  " Always display the status line
set autowrite     " Automatically :write before running commands
" set statusline=...[%{&fo}]...

" Softtabs, 4 spaces
set tabstop=8
set shiftwidth=4
set shiftround
set expandtab

" Make it obvious where 80 characters is
set textwidth=80
set colorcolumn=+1

" Numbers
" set number
" set numberwidth=5

augroup vimrcEx
  autocmd!

  " When editing a file, always jump to the last known cursor position.
  " Don't do it for commit messages, when the position is invalid, or when
  " inside an event handler (happens when dropping a file on gvim).
  autocmd BufReadPost *
    \ if &ft != 'gitcommit' && line("'\"") > 0 && line("'\"") <= line("$") |
    \   exe "normal g`\"" |
    \ endif

  " Set syntax highlighting for specific file types
  autocmd BufRead,BufNewFile Appraisals set filetype=ruby
  autocmd BufRead,BufNewFile *.md set filetype=markdown
  autocmd BufRead,BufNewFile .{jscs,jshint,eslint}rc set filetype=json

  " Setting for .md files
  autocmd BufRead,BufNewFile *.md setlocal textwidth=80
augroup END

" Display extra whitespace
set list listchars=tab:»·,trail:·,nbsp:·

" Use one space, not two, after punctuation.
set nojoinspaces

filetype plugin indent on

" Spell-check files
autocmd FileType markdown setlocal spell
autocmd FileType gitcommit setlocal spell

" Tab completion
" will insert tab at beginning of line,
" will use completion if not at beginning
set wildmode=list:longest,list:full
function! InsertTabWrapper()
    let col = col('.') - 1
    if !col || getline('.')[col - 1] !~ '\k'
        return "\<tab>"
    else
        return "\<c-p>"
    endif
endfunction
inoremap <Tab> <c-r>=InsertTabWrapper()<cr>
inoremap <S-Tab> <c-n>

" Switch between the last two files
nnoremap <leader><leader> <c-^>

" Set spellfile to location that is guaranteed to exist, can be symlinked to
" Dropbox or kept in Git and managed outside of thoughtbot/dotfiles using rcm.
set spelllang=en_us
set spellfile=$HOME/.vim-spell-en.utf-8.add

" Autocomplete with dictionary words when spell check is on
set complete+=kspell

" Switch syntax highlighting on, when the terminal has colors
" Also switch on highlighting the last used search pattern.
if (&t_Co > 2 || has("gui_running")) && !exists("syntax_on")
  syntax on
endif

" if filereadable(expand("~/.vimrc.bundles"))
"   source ~/.vimrc.bundles
" endif

" Load matchit.vim, but only if the user hasn't installed a newer version.
if !exists('g:loaded_matchit') && findfile('plugin/matchit.vim', &rtp) ==# ''
  runtime! macros/matchit.vim
endif

" Use The Silver Searcher https://github.com/ggreer/the_silver_searcher
"if executable('ag')
"  " Use Ag over Grep
"  set grepprg=ag\ --nogroup\ --nocolor
"
"  " Use ag in CtrlP for listing files. Lightning fast and respects .gitignore
"  let g:ctrlp_user_command = 'ag -Q -l --nocolor --hidden -g "" %s'
"
"  " ag is fast enough that CtrlP doesn't need to cache
"  let g:ctrlp_use_caching = 0
"endif

" Get off my lawn
" nnoremap <Left> :echoe "Use h"<CR>
" nnoremap <Right> :echoe "Use l"<CR>
" nnoremap <Up> :echoe "Use k"<CR>
" nnoremap <Down> :echoe "Use j"<CR>

" vim-rspec mappings
" nnoremap <Leader>t :call RunCurrentSpecFile()<CR>
" nnoremap <Leader>s :call RunNearestSpec()<CR>
" nnoremap <Leader>l :call RunLastSpec()<CR>

" Run commands that require an interactive shell
nnoremap <Leader>r :RunInInteractiveShell<space>

" Treat <li> and <p> tags like the block tags they are
let g:html_indent_tags = 'li\|p'

" Open new split panes to right and bottom, which feels more natural
set splitbelow
set splitright

" Always use vertical diffs
set diffopt+=vertical

" Quicker window movement
" nnoremap <C-j> <C-w>j
" nnoremap <C-k> <C-w>k
" nnoremap <C-h> <C-w>h
" nnoremap <C-l> <C-w>l

" configure syntastic syntax checking to check on open as well as save
let g:syntastic_check_on_open=1
let g:syntastic_html_tidy_ignore_errors=[" proprietary attribute \"ng-"]
let g:syntastic_eruby_ruby_quiet_messages =
    \ {"regex": "possibly useless use of a variable in void context"}

" Local config
" if filereadable($HOME . "/.vimrc.local")
"   source ~/.vimrc.local
" endif

" This will highlight all characters past 74 columns (tweak that number as
" desired) in dark grey (tweak that color as desired), and is a nice visual cue
" when auto linewrapping isn't turned on when you should think about breaking
" things.
"augroup vimrc_autocmds
"    autocmd BufEnter * highlight OverLength ctermbg=darkgrey guibg=#592929
"    autocmd BufEnter * match OverLength /\%74v.*/
"augroup END
