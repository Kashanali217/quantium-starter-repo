from dash.testing.application_runners import import_app


def test_header_present(dash_duo):
    app = import_app("my_dash_project.app")
    dash_duo.start_server(app)
    assert dash_duo.find_element("#header") is not None


def test_visualization_present(dash_duo):
    app = import_app("my_dash_project.app")
    dash_duo.start_server(app)
    assert dash_duo.find_element("#visualization") is not None


def test_region_picker_present(dash_duo):
    app = import_app("my_dash_project.app")
    dash_duo.start_server(app)
    assert dash_duo.find_element("#region-picker") is not None
