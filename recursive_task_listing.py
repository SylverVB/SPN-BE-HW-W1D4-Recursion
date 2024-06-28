# Lesson 6: Assignment | Recursion

# Recursive Task Listing

# Problem Statement: You are tasked with implementing a recursive function to list tasks within a hierarchical structure. Each task can have subtasks, forming a nested hierarchy. Your task is to design and implement a recursive function named list_tasks that traverses through the hierarchy and lists tasks in a structured manner.

task_hierarchy_1 = [
    {
        "name": "Project",
        "subtasks": [
            {"name": "Define project scope"},
            {"name": "Create project plan"},
            {"name": "Assign project team",
            "subtasks": [
                {"name": "Identify team members"},
                {"name": "Allocate roles and responsibilities"}
            ]},
            {"name": "Conduct project kickoff meeting"}
        ]
    },
    {
        "name": "Research",
        "subtasks": [
            {"name": "Gather data"},
            {"name": "Analyze data",
            "subtasks": [
                {"name": "Data cleaning"},
                {"name": "Statistical analysis"}
            ]},
            {"name": "Draw conclusions"}
        ]
    }
]

task_hierarchy_2 = [
    {
        "name": "Homework",
        "subtasks": [
            {"name": "Math assignment",
            "subtasks": [
                {"name": "Complete worksheet"},
                {"name": "Study for quiz"}
            ]},
            {"name": "History essay",
            "subtasks": [
                {"name": "Research topic"},
                {"name": "Write essay"}
            ]}
        ]
    },
    {
        "name": "Home project",
        "subtasks": [
            {"name": "Garden renovation",
            "subtasks": [
                {"name": "Design garden layout"},
                {"name": "Purchase plants and materials"}
            ]},
            {"name": "DIY furniture",
            "subtasks": [
                {"name": "Select furniture design"},
                {"name": "Buy materials"},
                {"name": "Assemble furniture"}
            ]}
        ]
    }
]

# Task 1: Design the Task Listing Function

# Design a Python function named list_tasks that takes a single parameter: task_hierarchy. The task_hierarchy parameter represents the nested hierarchy of tasks, where each task is a dictionary with the following keys:

# name: Name or description of the task.
# subtasks: List of subtasks (nested hierarchy), if any.
# The function should traverse through the task hierarchy recursively and list tasks along with their subtasks in a structured format.

# Task 2:  Implement Task Listing Logic

# Implement the task listing logic within the list_tasks function. Use recursion to traverse through the hierarchy and list tasks along with their subtasks. Print each task name and its subtasks (if any) with appropriate indentation to indicate the hierarchy.

# Task 3: Test the Task Scheduler Function

# Test your list_tasks function with various task hierarchies, including nested hierarchies with different levels of depth. Verify that tasks are listed correctly in a structured format.

# Expected Outcomes:

# Upon completing this assignment, students should be able to:

# Understand the concept of recursion and its application in traversing nested data structures.
#  Design and implement a recursive function to list tasks within a nested hierarchy
#  Test the task listing function with different task hierarchies to ensure correct behavior.
#  Gain confidence in using recursion to solve problems involving hierarchical data structures.


def list_tasks(task_hierarchy, indent=0):
    # Checking if task_hierarchy is not empty:
    if task_hierarchy:
        # Iterating over each item in task_hierarchy:
        for item in task_hierarchy:
            # Printing the name of the current task with the appropriate indentation:
            print(' ' * indent + f"- {item['name']}")
            # Checking if the current task has subtasks:
            if 'subtasks' in item:
                # Recursively listing the subtasks with increased indentation:
                list_tasks(item['subtasks'], indent + 2)  # Increasing the indent for nested subtasks
    else:
        print("No tasks yet")

print("Task Hierarchy 1:")
list_tasks(task_hierarchy_1)
print()
print("Task Hierarchy 2:")
list_tasks(task_hierarchy_2)