from awesome_panel.application.models import Author, Page, Tag


def test_can_construct_page(page):
    assert issubclass(type(page), Page)
    assert isinstance(page.name, str)
    assert isinstance(page.description, str)
    assert isinstance(page.author, Author)
    assert isinstance(page.description, str)
    assert isinstance(page.tags, list)
    assert isinstance(page.source_code_url, str)
    assert isinstance(page.thumbnail_png_url, str)
    assert hasattr(page, "component")
    assert page.show_loading_page == False
    assert page.restrict_max_width is True