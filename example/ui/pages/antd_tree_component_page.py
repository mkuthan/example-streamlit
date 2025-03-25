import streamlit as st
import streamlit_antd_components as sac


class TreeNode:
    def __init__(
        self, index, name, icon=None, description=None, tooltip=None, disabled=False, tags=None, children=None
    ):
        self.index = index
        self.name = name
        self.icon = icon
        self.description = description
        self.tooltip = tooltip
        self.disabled = disabled
        self.tags = tags or []
        self.children = children or []

    def __str__(self):
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


def convert_to_tree_items(nodes):
    items = []
    for node in nodes:
        sac_tags = []
        if node.tags:
            for tag in node.tags:
                if isinstance(tag, dict):
                    sac_tags.append(sac.Tag(tag.get("text", ""), color=tag.get("color", "blue")))
                else:
                    sac_tags.append(tag)

        children = convert_to_tree_items(node.children) if node.children else None

        item = sac.TreeItem(
            node.name,
            icon=node.icon,
            description=node.description,
            tooltip=node.tooltip,
            disabled=node.disabled,
            tag=sac_tags if sac_tags else None,
            children=children,
        )
        items.append(item)
    return items


def find_node_by_index(nodes, target_index):
    queue = list(nodes)

    while queue:
        node = queue.pop(0)
        if node.index == target_index:
            return node

        if node.children:
            queue.extend(node.children)

    return None


tree_data = [
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

st.title("AntD Tree Component")

left, center = st.columns([0.2, 0.8])

with left:
    tree_items = convert_to_tree_items(tree_data)
    selected_index = sac.tree(key="tree", items=tree_items, size="sm", open_all=True, return_index=True)

with center:
    if selected_index is None:
        st.write("Please select a node from the tree.")
    else:
        selected_node = find_node_by_index(tree_data, selected_index)
        if selected_node:
            st.subheader("Selected Node Details")
            st.write(selected_node)
