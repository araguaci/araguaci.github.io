---
layout: post
title: The Web’s Next Transition
subtitle: The web is made up of technologies that got their start over 25 years ago
cover-img: /assets/img/avatar-screenshot-med-26.jpg
thumbnail-img: /assets/img/chart.png
share-img: /assets/img/chart.png
tags: [websites, resources, productivity]
---

The web is made up of technologies that got their start over 25 years ago. HTTP, HTML, CSS, and JS were all first standardized in the mid-nineties (when I was 8 years old). Since then, the web evolved into a ubiquitous application platform. As the web has evolved, so too has the architecture for the development of these applications. There are many core architectures for building applications for the web these days. The most popular architecture employed by web developers today is the Single Page App (SPA), but **we are transitioning** to a new and improved architecture for building web applications.

The `<a>` and `<form>` elements have been around from the very beginning. Links for a browser to get things from a server, and forms for a browser to send things to a server (and get things in return). With this two-way communication established as a part of the specification from the start, it has been possible to create powerful applications on the web forever.

Here are the major architectures (in chronological order of popular use):

1.  Multi-Page Apps (MPAs)
2.  Progressively Enhanced Multi-Page Apps (PEMPAs, aka “JavaScript Sprinkles”)
3.  Single Page Apps (SPAs)
4.  _The next transition_

Each architecture of web development has benefits and pain points. Eventually, the pain points became enough of a problem to motivate the move to the next architecture which came with its own trade-offs.

No matter how we build our applications, we’re almost always going to need code running on a server (notable exceptions includes games like Wordle which \[_used to_\] store game state in local storage). One of the things that distinguishes these architectures is _where the code lives._ Let’s explore each of these in turn and watch how the location of code changed over time. As we cover each architecture, we’ll consider specifically the following use cases of code:

*   Persistence - saving and reading data from a database
*   Routing - directing traffic based on the URL
*   Data fetching - retrieving data from persistence
*   Data mutation - changing data in persistence
*   Rendering logic - displaying data to the user
*   UI Feedback - responding to user interaction

There are, naturally, more parts of a web application than these bits, but these are the bits that move around the most and where we spend the bulk of our time as web devs. Depending on project scale and team structure we may work in all of these categories of code or we may work on only a part of one.

**see in detail the diagrams and operation**

1.  [Multi-Page Apps (MPAs)](https://www.epicweb.dev/the-webs-next-transition#multi-page-apps-mpas)

    1.  [MPA Architectural Behaviors](https://www.epicweb.dev/the-webs-next-transition#mpa-architectural-behaviors)

    2.  [MPA Pros and cons](https://www.epicweb.dev/the-webs-next-transition#mpa-pros-and-cons)

2.  [Progressively Enhanced Multi-Page Apps (PEMPAs)](https://www.epicweb.dev/the-webs-next-transition#progressively-enhanced-multi-page-apps-pempas)

    1.  [PEMPA Architectural Behaviors](https://www.epicweb.dev/the-webs-next-transition#pempa-architectural-behaviors)

    2.  [PEMPA Pros and cons](https://www.epicweb.dev/the-webs-next-transition#pempa-pros-and-cons)

3.  [Single Page Apps (SPAs)](https://www.epicweb.dev/the-webs-next-transition#single-page-apps-spas)

    1.  [SPA Architectural Behaviors](https://www.epicweb.dev/the-webs-next-transition#spa-architectural-behaviors)

    2.  [SPA Pros and cons](https://www.epicweb.dev/the-webs-next-transition#spa-pros-and-cons)

4.  [Progressively Enhanced Single Page Apps (PESPAs)](https://www.epicweb.dev/the-webs-next-transition#progressively-enhanced-single-page-apps-pespas)

    1.  [PESPA Architectural Behaviors](https://www.epicweb.dev/the-webs-next-transition#pespa-architectural-behaviors)

    2.  [PESPA Pros and cons](https://www.epicweb.dev/the-webs-next-transition#pespa-pros-and-cons)

5.  [A PESPA Implementation: Remix](https://www.epicweb.dev/the-webs-next-transition#a-pespa-implementation-remix)

### Source:

 - [the-webs-next-transition](https://www.epicweb.dev/the-webs-next-transition)

