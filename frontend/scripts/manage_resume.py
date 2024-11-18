import os
import subprocess
import sys
from typing import Optional

class ResumeManager:
    def __init__(self):
        self.scripts_dir = os.path.dirname(os.path.abspath(__file__))
        self.frontend_dir = os.path.dirname(self.scripts_dir)
        
        # Ensure we're in the correct directory structure
        if not all(os.path.exists(os.path.join(self.frontend_dir, d)) 
                  for d in ['data', 'scripts', 'js']):
            raise RuntimeError("Invalid project structure. Please run from the frontend/scripts directory.")

    def _run_python_script(self, script_name: str) -> Optional[int]:
        """Run a Python script and return its exit code."""
        script_path = os.path.join(self.scripts_dir, script_name)
        if not os.path.exists(script_path):
            print(f"Error: Script {script_name} not found!")
            return None
        
        try:
            result = subprocess.run([sys.executable, script_path], check=True)
            return result.returncode
        except subprocess.CalledProcessError as e:
            print(f"Error running {script_name}: {str(e)}")
            return e.returncode
        except Exception as e:
            print(f"Unexpected error running {script_name}: {str(e)}")
            return None

    def main_menu(self):
        """Display and handle the main menu."""
        while True:
            print("\n=== Resume Management System ===")
            print("1. Manage Roles")
            print("2. Manage Projects")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == "1":
                print("\nLaunching Role Management System...")
                self._run_python_script("update_roles.py")
            elif choice == "2":
                print("\nLaunching Project Management System...")
                self._run_python_script("update_projects.py")
            elif choice == "3":
                print("\nExiting Resume Management System...")
                break
            else:
                print("\nInvalid choice! Please try again.")

def main():
    try:
        manager = ResumeManager()
        manager.main_menu()
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
