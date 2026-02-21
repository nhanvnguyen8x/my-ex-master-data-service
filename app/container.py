"""
Dependency container: default repository and service instances.

Use these in routes (and tests can override by injecting fakes).
Import: from app.container import category_service, tag_service, attribute_service
"""

from app.repositories import (
    CategoryRepository,
    TagRepository,
    AttributeRepository,
)
from app.services import CategoryService, TagService, AttributeService

# Default repositories
category_repository = CategoryRepository()
tag_repository = TagRepository()
attribute_repository = AttributeRepository()

# Default services (repos injected)
category_service = CategoryService(category_repository)
tag_service = TagService(tag_repository)
attribute_service = AttributeService(attribute_repository)
