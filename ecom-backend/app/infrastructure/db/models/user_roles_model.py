from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, UniqueConstraint
from sqlalchemy.orm import relationship
from app.infrastructure.db.base import Base

class UserRolesModel(Base):
    __tablename__ = 'user_roles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id', ondelete='CASCADE'), nullable=False)
    assigned_at = Column(DateTime, server_default=func.now(), nullable=False)

    # Evita duplicar roles por usuario
    __table_args__ = (
        UniqueConstraint('user_id', 'role_id', name='uq_user_role'),
    )
    user = relationship('UserModel', back_populates='user_roles')
    role = relationship('RoleModel', back_populates='user_roles')