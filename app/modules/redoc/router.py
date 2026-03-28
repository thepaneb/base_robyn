"""
Redoc module router.
"""

from robyn import SubRouter

router = SubRouter(file_object=__file__, prefix="/redoc")
