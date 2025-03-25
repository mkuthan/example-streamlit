class TreeNode:
    def __init__(
        self, index: int, name: str, icon=None, description=None, tooltip=None, disabled=False, tags=None, children=None
    ):
        self.index = index
        self.name = name
        self.icon = icon
        self.description = description
        self.tooltip = tooltip
        self.disabled = disabled
        self.tags = tags or []
        self.children = children or []

    def __str__(self) -> str:
        node_info = [f"TreeNode(index={self.index}, name='{self.name}')"]
        if self.description:
            node_info.append(f"description='{self.description}'")
        if self.icon:
            node_info.append(f"icon='{self.icon}'")
        if self.tooltip:
            node_info.append(f"tooltip='{self.tooltip}'")
        if self.disabled:
            node_info.append(f"disabled={self.disabled}")
        if self.tags:
            node_info.append(f"tags={self.tags}")
        if self.children:
            node_info.append(f"children=[{len(self.children)} items]")

        return f"{{{', '.join(node_info)}}}"


SAMPLE_TREE = [
    TreeNode(0, "item1", tags=[{"text": "Tag", "color": "red"}, {"text": "Tag2", "color": "cyan"}]),
    TreeNode(
        1,
        "item2",
        icon="apple",
        description="item description",
        children=[
            TreeNode(2, "tooltip", icon="github", tooltip="item tooltip"),
            TreeNode(
                3,
                "item2-2",
                children=[
                    TreeNode(4, "item2-2-1"),
                    TreeNode(5, "item2-2-2"),
                    TreeNode(6, "item2-2-3"),
                ],
            ),
        ],
    ),
    TreeNode(7, "disabled", disabled=True),
    TreeNode(
        8,
        "item3",
        children=[
            TreeNode(9, "item3-1"),
            TreeNode(10, "item3-2"),
        ],
    ),
]


def get_navigation_tree() -> list[TreeNode]:
    return SAMPLE_TREE
