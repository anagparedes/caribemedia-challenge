# Caribe Media Odoo Developer Test

This repository contains the solution to the Odoo Developer Challenge provided by Caribe Media. The purpose of this test is to evaluate coding and problem-solving skills, as well as the ability to work with Odoo.

## Requirements

- Odoo instance up and running (Version 15.0).
- Code organized with modularity and proper dependencies between modules.
- Clean and readable code.
- No unused code or files in custom modules.

## Getting Started

1. Set up your Odoo V15.0 instance using preferred method.
   - Recommended tools: VSCode as a code editor, Dockerdoo for running Odoo in Docker, and Dev Containers extension for faster development.

2. Create a database with the following details:
   - Country: Dominican Republic
   - Language: English

## Modules

### 1. Sales App Submodule (sale_management)

#### Sale Type Management

- Add a "sale_type" relational field with maintenance for user handling.
- If sale_type is "Recorded," make the "Call ID" field required in sales.
- If sale_type is "Signed," hide and make the "Call ID" field not required.
- Users can control the visibility of the "Call ID" field based on Sale Type maintenance.

### 2. Contacts App Submodule (contacts)

#### Multiple Phone Numbers Management

- Add necessary fields for managing multiple phone numbers dynamically per client.
  - Stored in the DB and visible only for Company clients.
- Store raw phone numbers without formatting.
- Include fields to indicate if a phone is active and if it is the main phone (only one main phone per client).
  
#### Access Rights

- Everyone can read/see all phones within the contact.
- Admin has full access to view and manage all additional phones.
- A group named "Phone Management" can read, add, and modify additional phones but cannot delete them.

### 3. Stock App Submodule (stock)

#### Search Filter

- Add a new search filter on the search bar to allow users to search by sale price.

#### Server Action for Contacts App

- Create a server action that adds the "Prospects" tag to the selected contact.
- The action must be available when the contact is selected.

#### Schedule Action for Contacts App

- Create a schedule action to update the "Notes" field of every contact.
- The action must add the text "Updated on {Day/Month/Year Hour:Minutes:Seconds}" to the Notes field.
- Schedule action executes every 1 minute.
- Schedule action stops when every contact has been updated.
- Schedule action updates only 2 contacts on every execution.

## Note

This repository may not contain all tasks, but the implemented tasks showcase my developer's skills and understanding of Odoo.
