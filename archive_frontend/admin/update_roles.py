import json
import os
from datetime import datetime
from typing import Dict, List, Optional

class RoleManager:
    def __init__(self, data_file: str, template_file: str, output_file: str):
        self.data_file = data_file
        self.template_file = template_file
        self.output_file = output_file
        self.roles_data = self._load_data()

    def _load_data(self) -> Dict:
        """Load roles data from JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {"roles": []}

    def _save_data(self):
        """Save roles data to JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.roles_data, f, indent=4)

    def add_role(self, 
                 category: str,
                 title: str,
                 company: str,
                 location: str,
                 date_start: str,
                 date_end: str = "present",
                 company_description: str = "",
                 job_description: str = "",
                 accomplishments: List[str] = None):
        """
        Add a new role to the data.
        
        Args:
            category: One of "administrative", "clinical", "academic"
            title: Job title
            company: Company name
            location: Job location
            date_start: Start date in YYYY-MM format
            date_end: End date in YYYY-MM format or "present"
            company_description: Description of the company
            job_description: Description of the role
            accomplishments: List of accomplishments/responsibilities
        """
        # Validate category
        if category not in ["administrative", "clinical", "academic"]:
            raise ValueError("Category must be one of: administrative, clinical, academic")

        # Format dates for display
        date_start_obj = datetime.strptime(date_start, "%Y-%m")
        date_start_display = date_start_obj.strftime("%B %Y")
        
        if date_end.lower() == "present":
            date_end_display = "Present"
        else:
            date_end_obj = datetime.strptime(date_end, "%Y-%m")
            date_end_display = date_end_obj.strftime("%B %Y")

        dates_display = f"{date_start_display} - {date_end_display}"

        # Create new role entry
        new_role = {
            "category": category,
            "date_start": date_start,
            "date_end": date_end,
            "title": title,
            "company": company,
            "location": location,
            "dates_display": dates_display,
            "company_description": company_description,
            "job_description": job_description,
            "accomplishments": accomplishments or []
        }

        # Add to roles list and sort by date
        self.roles_data["roles"].append(new_role)
        self.roles_data["roles"].sort(
            key=lambda x: (x["date_start"], x["date_end"]),
            reverse=True
        )
        self._save_data()

    def remove_role(self, company: str, title: str) -> bool:
        """Remove a role by company and title."""
        initial_length = len(self.roles_data["roles"])
        self.roles_data["roles"] = [
            role for role in self.roles_data["roles"]
            if not (role["company"] == company and role["title"] == title)
        ]
        if len(self.roles_data["roles"]) < initial_length:
            self._save_data()
            return True
        return False

    def update_role(self, company: str, title: str, updates: Dict) -> bool:
        """Update an existing role."""
        for role in self.roles_data["roles"]:
            if role["company"] == company and role["title"] == title:
                role.update(updates)
                self._save_data()
                return True
        return False

    def generate_html(self) -> str:
        """Generate HTML for all roles."""
        # Sort roles by category
        roles_by_category = {
            "administrative": [],
            "clinical": [],
            "academic": []
        }
        
        # Group roles by category
        for role in self.roles_data["roles"]:
            category = role["category"]
            if category in roles_by_category:
                roles_by_category[category].append(role)

        # Generate HTML for each category
        html_parts = []
        for category, roles in roles_by_category.items():
            if roles:  # Only add category if it has roles
                html_parts.append(f'<div class="category-section" id="{category}-roles">')
                html_parts.append(f'<h3>{category.title()} Roles</h3>')
                
                for role in roles:
                    accomplishments_html = "\n".join(
                        f'<li>{item}</li>' for item in role["accomplishments"]
                    )
                    
                    role_html = f'''
                        <div class="timeline-item" data-category="{role['category']}" data-date="{role['date_start']}">
                            <div class="role-title">{role['title']}</div>
                            <div class="company-name">{role['company']}</div>
                            <div class="role-meta">
                                <span class="dates">{role['dates_display']}</span>
                                <span class="location">{role['location']}</span>
                            </div>
                            <div class="company-description">
                                {role['company_description']}
                            </div>
                            <div class="job-description">
                                {role['job_description']}
                            </div>
                            <ul class="accomplishments">
                                {accomplishments_html}
                            </ul>
                        </div>
                    '''
                    html_parts.append(role_html)
                html_parts.append('</div>')  # Close category section

        return "\n".join(html_parts)

    def update_html_file(self):
        """Update the HTML file with generated role content."""
        if not os.path.exists(self.template_file):
            raise FileNotFoundError(f"Template file not found: {self.template_file}")

        try:
            with open(self.template_file, 'r', encoding='utf-8') as f:
                template_content = f.read()

            # Generate roles HTML
            roles_html = self.generate_html()

            # Look for the work experience section and insert roles
            start_marker = '<div class="work-experience" id="work-experience">'
            end_marker = '</div><!-- End of work experience -->'
            
            # Find the section and replace its content
            start_idx = template_content.find(start_marker)
            if start_idx == -1:
                raise ValueError("Could not find work experience section in template")
                
            end_idx = template_content.find(end_marker, start_idx)
            if end_idx == -1:
                raise ValueError("Could not find end of work experience section in template")
                
            # Construct the new content
            new_content = (
                template_content[:start_idx + len(start_marker)] +
                "\n" + roles_html + "\n" +
                template_content[end_idx:]
            )

            # Write the updated content
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"Successfully updated {self.output_file}")
            
        except Exception as e:
            print(f"Error updating HTML file: {str(e)}")
            raise

    def interactive_add_role(self):
        """Interactive command-line interface to add a role."""
        print("\n=== Add New Role ===")
        
        # Get role details
        category = input("Category (administrative/clinical/academic): ").lower()
        title = input("Job Title: ")
        company = input("Company Name: ")
        location = input("Location: ")
        date_start = input("Start Date (YYYY-MM): ")
        date_end = input("End Date (YYYY-MM or 'present'): ")
        
        print("\nCompany Description (press Enter twice when done):")
        company_description = []
        while True:
            line = input()
            if line:
                company_description.append(line)
            else:
                break
        company_description = " ".join(company_description)
        
        print("\nJob Description (press Enter twice when done):")
        job_description = []
        while True:
            line = input()
            if line:
                job_description.append(line)
            else:
                break
        job_description = " ".join(job_description)
        
        print("\nAccomplishments (one per line, press Enter twice when done):")
        accomplishments = []
        while True:
            line = input()
            if line:
                accomplishments.append(line)
            else:
                break

        # Add the role
        try:
            self.add_role(
                category=category,
                title=title,
                company=company,
                location=location,
                date_start=date_start,
                date_end=date_end,
                company_description=company_description,
                job_description=job_description,
                accomplishments=accomplishments
            )
            print("\nRole added successfully!")
        except Exception as e:
            print(f"\nError adding role: {str(e)}")

    def interactive_update_role(self):
        """Interactive interface to update a role."""
        print("\n=== Update Role ===")
        
        # List existing roles
        print("\nExisting Roles:")
        for i, role in enumerate(self.roles_data["roles"], 1):
            print(f"{i}. {role['company']} - {role['title']}")
        
        try:
            choice = int(input("\nSelect role to update (enter number): ")) - 1
            if choice < 0 or choice >= len(self.roles_data["roles"]):
                print("Invalid selection!")
                return
            
            role = self.roles_data["roles"][choice]
            
            # Show update menu
            while True:
                print("\nWhat would you like to update?")
                print("1. Title")
                print("2. Company")
                print("3. Location")
                print("4. Dates")
                print("5. Company Description")
                print("6. Job Description")
                print("7. Accomplishments")
                print("8. Done")
                
                update_choice = input("\nEnter choice (1-8): ")
                
                if update_choice == "1":
                    role["title"] = input("New Title: ")
                elif update_choice == "2":
                    role["company"] = input("New Company: ")
                elif update_choice == "3":
                    role["location"] = input("New Location: ")
                elif update_choice == "4":
                    role["date_start"] = input("New Start Date (YYYY-MM): ")
                    end = input("New End Date (YYYY-MM or 'present'): ")
                    role["date_end"] = end
                    date_start_obj = datetime.strptime(role['date_start'], "%Y-%m")
                    date_start_display = date_start_obj.strftime("%B %Y")
                    if role["date_end"].lower() == "present":
                        date_end_display = "Present"
                    else:
                        date_end_obj = datetime.strptime(role['date_end'], "%Y-%m")
                        date_end_display = date_end_obj.strftime("%B %Y")
                    role["dates_display"] = f"{date_start_display} - {date_end_display}"
                elif update_choice == "5":
                    role["company_description"] = input("New Company Description: ")
                elif update_choice == "6":
                    role["job_description"] = input("New Job Description: ")
                elif update_choice == "7":
                    print("\nCurrent Accomplishments:")
                    for i, acc in enumerate(role["accomplishments"], 1):
                        print(f"{i}. {acc}")
                    print("\nEnter new accomplishments (empty line to finish):")
                    new_acc = []
                    while True:
                        line = input("> ")
                        if not line:
                            break
                        new_acc.append(line)
                    if new_acc:
                        role["accomplishments"] = new_acc
                elif update_choice == "8":
                    break
                else:
                    print("Invalid choice!")
            
            # Save changes
            self._save_data()
            print("\nRole updated successfully!")
            
        except ValueError:
            print("Invalid input!")

def main():
    # Get the absolute path to the frontend directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    frontend_dir = os.path.dirname(current_dir)
    
    manager = RoleManager(
        data_file=os.path.join(frontend_dir, "data", "roles.json"),
        template_file=os.path.join(frontend_dir, "index_template.html"),
        output_file=os.path.join(frontend_dir, "index.html")
    )
    
    while True:
        print("\n=== Role Management System ===")
        print("1. Add New Role")
        print("2. Remove Role")
        print("3. Update Role")
        print("4. Generate HTML")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            manager.interactive_add_role()
        elif choice == "2":
            company = input("Company Name: ")
            title = input("Job Title: ")
            if manager.remove_role(company, title):
                print("Role removed successfully!")
            else:
                print("Role not found!")
        elif choice == "3":
            manager.interactive_update_role()
        elif choice == "4":
            manager.update_html_file()
            print("HTML generated successfully!")
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
