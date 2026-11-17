---
id: Dashboard
aliases:
  - Home
tags:
  - dashboard
---

# Dashboard

## Recent Daily Notes
```dataview
TABLE WITHOUT ID
  link(file.name, aliases[0]) AS "Date",
  join(filter(file.tags, (t) => startswith(t, "#customer/")), ", ") AS "Customers"
FROM "daily_notes/dailies"
WHERE contains(tags, "daily-notes")
SORT file.name DESC
LIMIT 15
```

## Customers
```dataview
TABLE WITHOUT ID
  file.link AS "Customer",
  join(file.tags, ", ") AS "Tags"
FROM "customers"
SORT file.name ASC
```

## Notes by Customer
> Click any customer tag below to see all related daily notes.

| Customer | Tag to search |
|----------|--------------|
| BlueYonder | `#customer/BlueYonder` |
| YayPay | `#customer/YayPay` |
| VENI | `#customer/VENI` |
| Keboola | `#customer/Keboola` |
| Analytics-Database | `#customer/Analytics-Database` |

## Recent 1-1 Meetings
```dataview
TABLE WITHOUT ID
  file.link AS "Meeting"
FROM "1-1Meeting"
SORT file.name DESC
LIMIT 5
```

[More 1-1 meeting notes in SharePoint](https://exasolcom-my.sharepoint.com/shared?listurl=https%3A%2F%2Fexasolcom%2Dmy%2Esharepoint%2Ecom%2Fpersonal%2Fmihai%5Fdinca%5Fexasol%5Fcom%2FDocuments&e=5%3Aa2816d33700446fea65576a37928ad38&sharingv2=true&fromShare=true&at=9&id=%2Fpersonal%2Fmihai%5Fdinca%5Fexasol%5Fcom%2FDocuments%2Fexasol%2F02%20Areas%2FEngineering%20Manager%2F1%2D1s%2FEdis&FolderCTID=0x0120003DCC495A0507054BA8DB2CEEAB878ABD)

## Open Tickets
```dataview
TABLE WITHOUT ID
  file.link AS "Ticket"
FROM "daily_notes/tickets"
SORT file.name ASC
```

## Weekly Notes
```dataview
TABLE WITHOUT ID
  file.link AS "Week"
FROM "weekly_notes"
SORT file.name DESC
LIMIT 10
```
