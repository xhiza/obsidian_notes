---
id: weekly-template
aliases: []
tags: []
---


<%*
const fileFormat = "[W]-YYYY-MM-WW" // Format for filename
const displayFormat = "YYYY-MM-[W]WW" // Format for display
const titleFormat = "[Week ]WW - MMMM YYYY" // Format for title
%>

# <% tp.date.now(titleFormat, 0) %> <!-- Title -->
week: <% tp.date.now(displayFormat, 0) %> <!-- Week Info -->

<< [[<% tp.date.now(fileFormat, -7) %>]] | [[<% tp.date.now(fileFormat, 7) %>]] >> <!-- Navigation Links -->

