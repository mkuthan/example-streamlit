import streamlit as st

from example.services import navigation_tree_service

# Initialize session state to track navigation
if "current_path" not in st.session_state:
    st.session_state.current_path = []  # List of node indices representing the path

# Get the navigation tree
navigation_tree = navigation_tree_service.get_navigation_tree()


# Function to find a node by index in the entire tree
def find_node_by_index(tree, target_index):
    for node in tree:
        if node.index == target_index:
            return node

        if node.children:
            result = find_node_by_index(node.children, target_index)
            if result:
                return result

    return None


# Function to get all nodes in the current path and the current node's children
def get_current_state():
    if not st.session_state.current_path:
        return None, navigation_tree

    # Get the current node based on the last index in the path
    current_node_index = st.session_state.current_path[-1]
    current_node = find_node_by_index(navigation_tree, current_node_index)

    if current_node:
        return current_node, current_node.children or []

    return None, navigation_tree


# Get current node and its children
current_node, children = get_current_state()

# Generate breadcrumbs text based on the path
breadcrumbs = []
for node_index in st.session_state.current_path:
    node = find_node_by_index(navigation_tree, node_index)
    if node:
        breadcrumbs.append(node.name)

# Add home icon to breadcrumbs
breadcrumbs_text = "🏠 Home" if not breadcrumbs else "🏠 Home -> " + " -> ".join(breadcrumbs)

st.title("Breadcrumbs Navigation Page")
st.subheader(breadcrumbs_text)

left, center = st.columns([0.2, 0.8])

with left:
    # Display the children of the current node or the top-level nodes
    for node in children:
        # Add a prefix to indicate if the node has children
        prefix = "📁 " if node.children else "📄 "

        # Create a clickable button for each node
        if st.button(f"{prefix}{node.name}", key=f"btn_{node.index}", disabled=node.disabled):
            st.session_state.current_path.append(node.index)
            st.rerun()

    # Add a "Go up" button if not at the root level
    if st.session_state.current_path and st.button("⬆️ Go Up"):
        st.session_state.current_path.pop()
        st.rerun()

with center:
    if current_node:
        st.header(current_node.name)

        # Display node details
        if current_node.description:
            st.write(f"**Description:** {current_node.description}")

        if current_node.tooltip:
            st.write(f"**Tooltip:** {current_node.tooltip}")

        if current_node.icon:
            st.write(f"**Icon:** {current_node.icon}")

        if current_node.tags:
            st.write("**Tags:**")
            for tag in current_node.tags:
                st.write(f"- {tag['text']} ({tag['color']})")
    else:
        st.write("Please select a node from the tree.")
