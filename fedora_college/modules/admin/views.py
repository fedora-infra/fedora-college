# -*- coding: utf-8 -*-
from flask import g
from flask.ext import admin
from flask.ext.admin.contrib import sqla
from flask.ext.admin import expose
from flask.ext.admin.contrib.fileadmin import FileAdmin

# Create customized index view class that handles login & registration


class FedoraModelView(sqla.ModelView):
    column_display_pk = True
    column_display_pk = True

    def is_accessible(self):
        try:
            groups = list(g.fas_user['groups'])
            if len(groups) > 0:
                return True
            else:
                return False
        except:
            return False


class FedoraFileView(FileAdmin):

    def is_accessible(self):
        try:
            groups = list(g.fas_user['groups'])
            if len(groups) > 0:
                return True
            else:
                return False
        except:
            return False


class FedoraAdminIndexView(admin.AdminIndexView):

    column_display_pk = True
    column_display_fk = True

    def is_accessible(self):
        try:
            groups = list(g.fas_user['groups'])
            if len(groups) > 0:
                return True
            else:
                return False
        except:
            return False

    @expose('/')
    def index(self):
        try:
            if g.fas_user.username:
                return super(FedoraAdminIndexView, self).index()
            return str(self.is_accessible())
        except:
            return "404"
