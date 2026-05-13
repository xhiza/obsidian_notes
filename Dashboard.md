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
