from dpatterns_python import composite


def test_component_function():
    sub1 = composite.Composite("submenu1")

    sub11 = composite.Child("sub_submenu 11")

    sub12 = composite.Child("sub_submenu 12")

    sub1.append_child(sub11)

    sub1.append_child(sub12)

    top = composite.Composite("top_menu")

    sub2 = composite.Child("submenu2")

    top.append_child(sub1)

    top.append_child(sub2)

    top.component_function()
