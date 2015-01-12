Help Base
========================

### An attempt to implement DDD and hexagonal architecture in Python using Django framework w/o replacing Django's core components.

Domain
========================

- A customer should be able to create a ticket.
- A customer should have an email address, first name and last name. An email address should always be present.
- Customer records should be unique. When a customer creates a ticket for the first time, a record of that customer will be created. This record will be used for the next tickets that he creates.
- A ticket should have a title and a body. A title should always be present.
- A ticket is assigned a Staffer at some point (not on creation).
- A staffer can assign himself to a ticket. Only one staffer is allowed to be assigned on each ticket.
- A staffer or a customer can close a ticket.
- If a ticket has a status of "closed", any newly received message will re-open the ticket.
