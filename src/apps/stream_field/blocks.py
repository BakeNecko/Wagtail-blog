from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True)

    class Meta:
        template = "title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Под-Заголовок в статье отображаемый по Центру"


class GithubCommitBlock(blocks.StructBlock):
    commit_link = blocks.URLBlock(required=True)

    class Meta:
        template = "github_link_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Под-Заголовок в статье отображаемый по Центру"


class TextBlock(blocks.StructBlock):
    """ Блок с куском кода """
    text = blocks.RichTextBlock(required=True)

    class Meta:
        template = "text_block.html"
        icon = "edit"
        label = "Text-Block RichText"
        help_text = "Создать кусок текста"


class IMGBlock(blocks.StructBlock):
    """ Блок с куском кода """
    img = ImageChooserBlock()
    img_description = blocks.CharBlock(required=False)

    class Meta:
        template = "img_block.html"
        icon = "edit"
        label = "Img-Block RichText"
        help_text = "Создать Вставку с Картинкой"


class CodeBlock(blocks.StructBlock):
    """ Блок с куском кода """
    code_text = blocks.RichTextBlock(required=True)

    class Meta:
        template = "code_block.html"
        icon = "edit"
        label = "Code-Block RichText"
        help_text = "Создать кусок кода"

