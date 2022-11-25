from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

def create_map():
    if request.method == "POST":
       NodeName = request.form['NodeName']
