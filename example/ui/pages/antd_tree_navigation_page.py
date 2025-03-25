import streamlit as st
import streamlit_antd_components as sac

from example.services import navigation_tree_service


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


st.title("AntD Tree Navigation Page")

navigation_tree = navigation_tree_service.get_navigation_tree()

left, center = st.columns([0.2, 0.8])

with left:
    tree_items = convert_to_tree_items(navigation_tree)
    selected_index = sac.tree(key="tree", items=tree_items, size="sm", open_all=True, return_index=True)

with center:
    if selected_index is None:
        st.write("Please select a node from the tree.")
    else:
        selected_node = find_node_by_index(navigation_tree, selected_index)
        if selected_node:
            st.subheader("Selected Node Details")
            st.write(selected_node)
