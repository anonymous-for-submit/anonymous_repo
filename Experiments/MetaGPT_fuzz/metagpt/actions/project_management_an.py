#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/12/14 15:28
@Author  : alexanderwu
@File    : project_management_an.py
"""
from typing import List, Optional

from metagpt.actions.action_node import ActionNode

REQUIRED_PACKAGES = ActionNode(
    key="Required packages",
    expected_type=Optional[List[str]],
    instruction="Provide required packages from standard library of python if needed.",
    example=["No required packages"],
)

REQUIRED_OTHER_LANGUAGE_PACKAGES = ActionNode(
    key="Required Other language third-party packages",
    expected_type=List[str],
    instruction="Please state that no other packages are provided",
    example=["No third-party dependencies required"],
)

LOGIC_ANALYSIS = ActionNode(
    key="Logic Analysis",
    expected_type=List[List[str]],
    instruction="Provide one main.py file to be implemented, make sure only use the standard library"
    "including dependency analysis and imports.",
    example=[
        ["main.py", "Contains one function with the same input/output format as user requirment"],
    ],
)

# LOGIC_ANALYSIS = ActionNode(
#     key="Logic Analysis",
#     expected_type=List[List[str]],
#     instruction="Provide one main.py file to be implemented, make sure only use the standard library. Use input() to read from io and print() to output the result"
#     "including dependency analysis and imports.",
#     example=[
#         ["main.py", "Contains one function with the same input/output format as user requirment, use input() to read input, print() to print the output"],
#     ],
# )

REFINED_LOGIC_ANALYSIS = ActionNode(
    key="Refined Logic Analysis",
    expected_type=List[List[str]],
    instruction="Review and refine the logic analysis by merging the Legacy Content and Incremental Content. "
    "Provide a comprehensive list of files with classes/methods/functions to be implemented or modified incrementally. "
    "Include dependency analysis, consider potential impacts on existing code, and document necessary imports.",
    example=[
        ["game.py", "Contains Game class and ... functions"],
        ["main.py", "Contains main function, from game import Game"],
        ["new_feature.py", "Introduces NewFeature class and related functions"],
        ["utils.py", "Modifies existing utility functions to support incremental changes"],
    ],
)

TASK_LIST = ActionNode(
    key="File list",
    expected_type=List[str],
    instruction="Only include main.py",
    example=["main.py"],
)

REFINED_TASK_LIST = ActionNode(
    key="Refined File list",
    expected_type=List[str],
    instruction="Review and refine the combined task list after the merger of Legacy Content and Incremental Content, "
    "and consistent with Refined File List. Ensure that tasks are organized in a logical and prioritized order, "
    "considering dependencies for a streamlined and efficient development process. ",
    example=["new_feature.py", "utils", "game.py", "main.py"],
)

FULL_API_SPEC = ActionNode(
    key="Full API spec",
    expected_type=str,
    instruction="Describe all APIs using OpenAPI 3.0 spec that may be used by both frontend and backend. If front-end "
    "and back-end communication is not required, leave it blank.",
    example="openapi: 3.0.0 ...",
)

SHARED_KNOWLEDGE = ActionNode(
    key="Shared Knowledge",
    expected_type=str,
    instruction="Detail any shared knowledge, like common utility functions or configuration variables.",
    example="",
)

REFINED_SHARED_KNOWLEDGE = ActionNode(
    key="Refined Shared Knowledge",
    expected_type=str,
    instruction="Update and expand shared knowledge to reflect any new elements introduced. This includes common "
    "utility functions, configuration variables for team collaboration. Retain content that is not related to "
    "incremental development but important for consistency and clarity.",
    example="`new_module.py` enhances shared utility functions for improved code reusability and collaboration.",
)


ANYTHING_UNCLEAR_PM = ActionNode(
    key="Anything UNCLEAR",
    expected_type=str,
    instruction="Mention any unclear aspects in the project management context and try to clarify them.",
    example="Clarification needed on how to start and initialize third-party libraries.",
)

NODES = [
    REQUIRED_PACKAGES,
    REQUIRED_OTHER_LANGUAGE_PACKAGES,
    LOGIC_ANALYSIS,
    TASK_LIST,
    FULL_API_SPEC,
    SHARED_KNOWLEDGE,
    ANYTHING_UNCLEAR_PM,
]

REFINED_NODES = [
    REQUIRED_PACKAGES,
    REQUIRED_OTHER_LANGUAGE_PACKAGES,
    REFINED_LOGIC_ANALYSIS,
    REFINED_TASK_LIST,
    FULL_API_SPEC,
    REFINED_SHARED_KNOWLEDGE,
    ANYTHING_UNCLEAR_PM,
]

PM_NODE = ActionNode.from_children("PM_NODE", NODES)
REFINED_PM_NODE = ActionNode.from_children("REFINED_PM_NODE", REFINED_NODES)
