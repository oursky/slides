# Install vim-pathogen

	mkdir -p ~/.vim/autoload ~/.vim/bundle; \
	curl -so ~/.vim/autoload/pathogen.vim \
		https://raw.github.com/tpope/vim-pathogen/master/autoload/pathogen.vim`

Edit ~/.vimrc, put the following line:

	call pathogen#infect()
	syntax on
	filetype plugin indent on

# Use git to handle your .vim directory

In your ~/.vim, do the following to create a git repo for your vim configs

	git init
	git submodule add https://github.com/kien/ctrlp.vim.git bundle/ctrlp
	git submodule init
	git commit -a -m "Added ctrlp"



# .vimrc must have:

	filetype on
	set nocompatible 
	set modelines=1 (N)
	set clipboard+=unnamed " Yanks go on clipboard instead.
	set history=256  " Number of things to remember in history.
	set ruler  " Ruler on
	set nu " Line numbers on
	set nowrap " Line wrapping off
	set hlsearch " highlight all its previous search match
	set incsearch " show match while typing search
	set ignorecase " for search
	set smartcase " override ignorecase for upper character
	set ts=2
	set shiftwidth=2
	set bs=2
	set formatoptions=tcqr " see fo-table and paste options
	set cindent
	set autoindent
	set smarttab
	set expandtab
	set showmatch " highlight matching indent
	set novisualbell  " No blinking .
	set noerrorbells  " No noise.
	set laststatus=2  " Always show status line.

	match OverLength /\%81v.\+/
	highlight OverLength ctermbg=red ctermfg=white guibg=#592929

	filetype plugin indent on " Enable filetype-specific indenting and plugins
	autocmd FileType ruby,eruby,yaml set ts=2 shiftwidth=2  " Tabs are 2 spaces
	autocmd FileType python set ts=4 shiftwidth=4  " Tabs are 4 spaces

	set backupdir=~/.vim/backup
	set directory=~/.vim/backup

# Vim Plugins

## Must have
* vim-pathogen
* command-t / ctrlp		- fuzzy finder
* fugitive.vim				- git

## Python
* python.vim					- python syntax highlight
* pyflakes						- live python compile
* pep8
* vim-virtualenv			- works with virtualenvwrapper

## Other
* rubycomplete.vim		- ruby auto complete
* vim-ruby					
* vim-coffee-script 	- CoffeeCompile watch
* simple-javascript-indenter

## Maybe
* delimitmate					- Add closing brackets
* HTML-AutoCloseTag		- Add closing HTML tags
* IndentAnything
* vim-powerline				- Better status line
* supertab

## Interesting
* NerdCommenter
* NerdTree
* zencoding-vim
* vim-rails

# More!
http://www.viemu.com/a-why-vi-vim.html