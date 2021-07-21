#!/bin/bash

coverage-3.9 run --source myproject.production -m unittest discover && coverage-3.9 report