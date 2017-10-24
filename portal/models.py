from portal import *

class PortalCategory(MainModel):
    name = Column(UnicodeText)
    key = Column(UnicodeText)
    items = relationship('PortalItem', backref='category')
    public = Column(Boolean, default=True)

class PortalItem(MainModel):
    name = Column(UnicodeText)
    link = Column(UnicodeText)
    key = Column(UnicodeText)
    category_id = Column(UUID, ForeignKey('portal_category.id'))
    public = Column(Boolean, default=True)
