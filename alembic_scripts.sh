#!/bin/bash
alembic -n alembic:dev revision --autogenerate
alembic -n alembic:dev upgrade head