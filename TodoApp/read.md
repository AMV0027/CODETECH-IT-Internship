**Documentation: To-Do App**

**Overview:**
This documentation outlines the structure and functionality of a simple To-Do application built using Flask, HTML, and Tailwind CSS. The application allows users to add tasks with details such as category, due date, priority, and notes. Users can mark tasks as completed, and completed tasks are displayed separately.

**Tech Stack:**
- Flask: A micro web framework for Python used for building web applications.
- HTML: Hypertext Markup Language used for structuring web pages.
- Tailwind CSS: A utility-first CSS framework used for styling web applications.

**Files:**
1. **app.py**: Contains the Flask application code.
2. **index.html**: HTML template for the main page of the application.
3. **completed.html**: HTML template for the completed tasks page.

**Functionality:**

1. **Main Page (/)**:
   - Displays a list of tasks to be completed.
   - Allows users to add new tasks with details such as name, category, due date, priority, and notes.
   - Each task card includes options to mark the task as completed or remove it.

2. **Add Task (/add)**:
   - Accepts POST requests to add a new task to the list.
   - Retrieves task details from the submitted form data.
   - Appends the task to the list of tasks and redirects to the main page.

3. **Remove Task (/remove/<int:index>)**:
   - Accepts POST requests to remove a task from the list.
   - Retrieves the index of the task to be removed.
   - Removes the task from the list of tasks and appends it to the list of completed tasks.

4. **Completed Tasks Page (/completed)**:
   - Displays a list of completed tasks.
   - Each completed task card includes details such as name, category, due date, priority, and notes.

**HTML Templates:**
- **index.html**:
  - Includes a form for adding new tasks.
  - Displays a list of tasks with options to mark as completed or remove.
- **completed.html**:
  - Displays a list of completed tasks.

**Styling:**
- **Tailwind CSS** is used for styling the application, providing a clean and modern interface.
- CSS classes from Tailwind CSS are applied directly to HTML elements to style the components.

**Running the Application:**
- Ensure Flask and other dependencies are installed.
- Run the `app.py` file.
- Access the application through a web browser.

This documentation provides an overview of the structure, functionality, and technologies used in the To-Do application, facilitating understanding and further development or customization.
