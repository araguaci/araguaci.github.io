---
layout: post
title: The only Linux command you need to know
subtitle: The Linux cheat command is a utility to search
cover-img: /assets/img/new-future-technology.jpg
thumbnail-img: /assets/img/tux.png
share-img: /assets/img/tux.png
tags: [linux, opensource]
---


The Linux cheat command is a utility to search for and display a list of example tasks you might do with a command.

By [Seth Kenlon](https://opensource.com/users/seth) (Team, Red Hat)


![Command line prompt](https://opensource.com/sites/default/files/lead-images/command_line_prompt.png "Command line prompt")

Image by:
Opensource.com

Information about Linux and open source abounds on the internet, but when you're entrenched in your work there's often a need for quick documentation. Since the early days of Unix, well before Linux even existed, there's been the `man` (short for "manual") and `info` commands, both of which display official project documentation about commands, configuration files, system calls, and more.

There's a debate over whether `man` and `info` pages are meant as helpful reminders for users who already know how to use a tool, or an intro for first time users. Either way, both `man` and `info` pages describe tools and how to use them, and rarely address specific tasks and how to accomplish them. It's for that very reason that the `cheat` command was developed.

For instance, suppose you can't remember how to [unarchive a tar file](https://opensource.com/article/17/7/how-unzip-targz-file). The `man` page provides you with all the options you require, but it leaves it up to you to translate this information into a functional command:

tar \-A \[OPTIONS\] ARCHIVE ARCHIVE  
tar \-c \[\-f ARCHIVE\] \[OPTIONS\] \[FILE...\]  
tar \-d \[\-f ARCHIVE\] \[OPTIONS\] \[FILE...\]  
tar \-t \[\-f ARCHIVE\] \[OPTIONS\] \[MEMBER...\]  
tar \-r \[\-f ARCHIVE\] \[OPTIONS\] \[FILE...\]  
tar \-u \[\-f ARCHIVE\] \[OPTIONS\] \[FILE...\]  
tar \-x \[\-f ARCHIVE\] \[OPTIONS\] \[MEMBER...\]

That's exactly what some users need, but it confounds other users. The cheat sheet for tar, by contrast, provides complete common commands:

```
$ cheat tar  
```
  
```
\# To extract an uncompressed archive:  
tar \-xvf /path/to/foo.tar  
  
\# To extract a .tar in specified Directory:  
tar \-xvf /path/to/foo.tar \-C /path/to/destination/  
  
\# To create an uncompressed archive:  
tar \-cvf /path/to/foo.tar /path/to/foo/  
  
\# To extract a .tgz or .tar.gz archive:  
tar \-xzvf /path/to/foo.tgz  
tar \-xzvf /path/to/foo.tar.gz  
\[...\]
```

It's exactly what you need, when you need it.

More Linux resources

[Linux commands cheat sheet](https://developers.redhat.com/cheat-sheets/linux-commands-cheat-sheet/?intcmp=70160000000h1jYAAQ)

[Advanced Linux commands cheat sheet](https://developers.redhat.com/cheat-sheets/advanced-linux-commands/?intcmp=70160000000h1jYAAQ)

[Free online course: RHEL technical overview](https://www.redhat.com/en/services/training/rh024-red-hat-linux-technical-overview?intcmp=70160000000h1jYAAQ)

[Linux networking cheat sheet](https://opensource.com/downloads/cheat-sheet-networking?intcmp=70160000000h1jYAAQ)

[SELinux cheat sheet](https://opensource.com/downloads/cheat-sheet-selinux?intcmp=70160000000h1jYAAQ)

[Linux common commands cheat sheet](https://opensource.com/downloads/linux-common-commands-cheat-sheet?intcmp=70160000000h1jYAAQ)

[What are Linux containers?](https://opensource.com/resources/what-are-linux-containers?intcmp=70160000000h1jYAAQ)

[Our latest Linux articles](https://opensource.com/tags/linux?intcmp=70160000000h1jYAAQ)

The Linux cheat command
-----------------------

The `cheat` command is a utility to search for and display a list of example tasks you might do with a Linux command. As with many Unix commands, there are different implementations of the same concept, including one [written in Go](https://github.com/cheat/cheat) and one, which I help maintain, [written in just 100 lines of Bash](https://gitlab.com/slackermedia/cheat).

To install the Go version, download [the latest release](https://github.com/cheat/cheat/releases) and put it somewhere in [your path](https://opensource.com/article/17/6/set-path-linux), such as `~/.local/bin/` or `/usr/local/bin`. To install the Bash version, download the latest release and run the `install-cheat.sh` script:

`$ sh ./install-cheat.sh`

Or to configure the installation, use [Autotools](https://opensource.com/article/19/7/introduction-gnu-autotools):

```
$ aclocal ; autoconf  
$ automake \--add-missing ; autoreconf  
$ ./configure \--prefix\=$HOME/.local  
$ make  
$ make install
```

Get cheat sheets for your Linux terminal
----------------------------------------

Cheat sheets are just plain text files containing common commands. The main collection of cheat sheets is available at [Github.com/cheat/cheatsheets](https://github.com/cheat/cheatsheets). The Go version of cheat downloads cheatsheets for you when you first run the command. If you're using the Bash version of cheat, the `--fetch` option downloads cheatsheets for you:

`$ cheat --fetch`

As with `man` pages, you can have multiple collections of cheat sheets on your system. The Go version of cheat uses a [YAML](https://opensource.com/article/21/9/yaml-cheat-sheet) config file to define where each collection is located. The Bash version defines the path during the install, and by default downloads the [Github.com/cheat/cheatsheets](https://github.com/cheat/cheatsheets) collection as well as [Opensource.com](http://Opensource.com)'s own [Gitlab.com/opensource.com/cheatsheets](https://gitlab.com/opensource.com/cheatsheets) collection.

List cheat sheets
-----------------

To list the cheat sheets on your system, use the `--list` option:

```
$ cheat \--list  
```

```
7z  
ab  
acl  
alias  
ansi  
ansible  
ansible-galaxy  
ansible-vault  
apk  
\[...\]
```

View a Linux cheat sheet
------------------------

Viewing a cheat sheet is as easy as viewing a `man` or `info` page. Just provide the name of the command you need help with:

```
$ cheat alias  
```
  
\# To show a list of your current shell aliases:  
alias  
  
\# To alias \`ls -l\` to \`ll\`:  
alias ll\='ls -l'

By default, the `cheat` command uses your environment's pager. Your pager is set with the `PAGER` [environment variable](https://opensource.com/article/19/8/what-are-environment-variables). You can override that temporarily by redefining the `PAGER` variable before running the `cheat` command:

`$ PAGER=most cheat less`

If you just want to [cat](https://opensource.com/article/19/2/getting-started-cat-command) the cheat sheet into your terminal without a pager, the Bash version has a `--cat` option for convenience:

`$ cheat --cat less`

It's not actually cheating
--------------------------

The cheat system cuts to the chase. You don't have to piece together clues about how to use a command. You just follow the examples. Of course, for complex commands, it's not a shortcut for a thorough study of the actual documentation, but for quick reference, it's as fast as it gets.

You can even create your own cheat sheet just by placing a file in one of the cheat sheet collections. Good news! Because the projects are open source, you can contribute your personal cheat sheets to the GitHub collection. And more good news! When there's a new Opensource.com [cheat sheet](https://opensource.com/downloads) release, we'll include a plain text version from now on so you can add that to your collection.

The command is called `cheat`, but as any Linux user will assure you, it's not actually cheating. It's working smarter, the open source way.

What to read next

Tags

[Linux](https://opensource.com/tags/linux)

[Seth Kenlon](https://opensource.com/users/seth)

![Seth Kenlon](https://opensource.com/sites/default/files/styles/150x150/public/pictures/seth_headshot-lawrence_0.jpg?itok=jZUHBHx4)

Seth Kenlon is a UNIX geek, free culture advocate, independent multimedia artist, and D&D nerd. He has worked in the film and computing industry, often at the same time.

[More about me](https://opensource.com/users/seth)

6 Comments
----------

These comments are closed, however you can [Register](https://opensource.com/user/register?absolute=1) or [Login](https://opensource.com/user/login?current=/node/70039&absolute=1) to post a comment on another article.

![Avatar](https://opensource.com/sites/default/files/styles/medium/public/osdc_default_avatar_1.png?itok=G0WcUo3c "Avatar")

[Charlie Arehart](https://opensource.com/users/carehart) | June 2, 2022

Thanks, Seth. Your posts here offer so much great info. As for this, I'll point out a similar cmd I've long used, tldr. I'm writing on my phone as I see this, so I can't readily compare their results. Just wanted to mention it, if it may help anyone. Looking forward to checking out cheat, also.

![Seth Kenlon](https://opensource.com/sites/default/files/styles/medium/public/pictures/seth_headshot-lawrence_0.jpg?itok=95gfWZwd)

[Seth Kenlon](https://opensource.com/users/seth) | June 2, 2022

This is great!  I hadn't heard about tldr but I'm definitely going to check it out now.

[https://tldr.sh/](https://tldr.sh/)

Thanks for the tip, Charlie!

In reply to [Thanks, Seth. Your posts…](https://opensource.com/comment/219565#comment-219565) by [Charlie Arehart](https://opensource.com/users/carehart "View user profile.")

![](https://opensource.com/sites/default/files/styles/medium/public/pictures/profile_pic_1.jpg?itok=064Ko9DF)

[Peter Cheer](https://opensource.com/users/petercheer) | June 6, 2022

Thanks Seth. I have a bunch of students who have just finished their 'Operating Systems' block but I shall point them all to this anyway, even if I normally tell them not to cheat.

![Avatar](https://opensource.com/sites/default/files/styles/medium/public/osdc_default_avatar_1.png?itok=G0WcUo3c "Avatar")

[John Curwood](https://opensource.com/users/blindape) | June 8, 2022

This is fantastic. I can't count the number of times I have stared at a man page trying to figure out how I am supposed to use a command.

![Avatar](https://opensource.com/sites/default/files/styles/medium/public/osdc_default_avatar_1.png?itok=G0WcUo3c "Avatar")

[Hector Rod](https://opensource.com/users/hectorrod) | June 10, 2022

Saved! Excellent resource, thanks so much Seth.

![Avatar](https://opensource.com/sites/default/files/styles/medium/public/osdc_default_avatar_1.png?itok=G0WcUo3c "Avatar")

[wisnoskij](https://opensource.com/users/wisnoskij) | July 9, 2022

Hmm, based on the output this seems completely separate form tldr.

But also, what is with that tar command. Even example used like 4 modifiers, wow, we really need a better way to deal with archives on Linux. The gui programs suck, and this is almost worse, expecting every single use of the command to include so many arguments.

Related Content
---------------

[![Mesh networking connected dots](https://opensource.com/sites/default/files/styles/222x125/public/lead-images/mesh_networking_dots_connected.png?itok=Kr2O2nQn "Mesh networking connected dots")](https://opensource.com/article/22/9/ebpf-monitor-traffic-tracee)

[How Tracee solves the lack of BTF information](https://opensource.com/article/22/9/ebpf-monitor-traffic-tracee)

[![Two people chatting via a video conference app](https://opensource.com/sites/default/files/styles/222x125/public/lead-images/chat_video_conference_talk_team.png?itok=umVvqFEf "Two people chatting via a video conference app")](https://opensource.com/article/22/8/share-screens-linux-gnome-connections)

[Share screens on Linux with GNOME Connections](https://opensource.com/article/22/8/share-screens-linux-gnome-connections)

[![women programming](https://opensource.com/sites/default/files/styles/222x125/public/lead-images/collab-team-pair-programming-code-keyboard2.png?itok=sKbhNMzu "women programming")](https://opensource.com/article/22/8/linux-tar-command)

[4 ways to use the Linux tar command](https://opensource.com/article/22/8/linux-tar-command)

[![Creative Commons License](https://opensource.com/themes/osdc/assets/img/cc-by-sa-4.png "This work is licensed under a Creative Commons Attribution-Share Alike 4.0 International License.")](http://creativecommons.org/licenses/by-sa/4.0/)This work is licensed under a Creative Commons Attribution-Share Alike 4.0 International License.

[Source](https://opensource.com/article/22/6/linux-cheat-command)