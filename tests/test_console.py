#!/usr/bin/python3

import unittest
import sys
import io
from contextlib import contextmanager
from models import *
from datetime import datetime
from console import HBNBCommand
from models.base_model import BaseModel


@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class Test_Console(unittest.TestCase):
    """
    Test the console
    """

    def setUp(self):
        self.cli = HBNBCommand()

        test_args = {'updated_at': datetime(2017, 2, 11, 23, 48, 34, 339879),
                     'id': 'd3da85f2-499c-43cb-b33d-3d7935bc808c',
                     'created_at': datetime(2017, 2, 11, 23, 48, 34, 339743),
                     'name': 'Ace'}
        self.model = BaseModel(test_args)
        self.model.save()

    def tearDown(self):
        self.cli.do_destroy("BaseModel d3da85f2-499c-43cb-b33d-3d7935bc808c")

    def test_show_error_no_args(self):
        with captured_output() as (out, err):
            self.cli.onecmd("show ''")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_error_missing_arg(self):
        with captured_output() as (out, err):
            self.cli.onecmd("show BaseModel")
        output = out.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_show_error_invalid_class(self):
        with captured_output() as (out, err):
            self.cli.onecmd("show Human 1234-5678-9101")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

        with captured_output() as (out, err):
            self.cli.onecmd("create BaseModel")
        output = out.getvalue().strip()

        with captured_output() as (out, err):
            self.cli.onecmd("show BaseModel {}".format(output))
        output2 = out.getvalue().strip()
        self.assertTrue(output in output2)

    def test_destroy_correct(self):
        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900)}
        testmodel = BaseModel(test_args)
        testmodel.save()
        self.cli.onecmd("destroy BaseModel f519fb40-1f5c-458b-945c-2ee8eaaf4900")

        with captured_output() as (out, err):
            self.cli.onecmd("show BaseModel f519fb40-1f5c-458b-945c-2ee8eaaf4900")
        output = out.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_destroy_error_missing_id(self):
        with captured_output() as (out, err):
            self.cli.onecmd("destroy BaseModel")
        output = out.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_destroy_error_invalid_class(self):
        with captured_output() as (out, err):
            self.cli.do_destroy("Human d3da85f2-499c-43cb-b33d-3d7935bc808c")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_error_invalid_id(self):
        with captured_output() as (out, err):
            self.cli.do_destroy("BaseModel " +
                                "f519fb40-1f5c-458b-945c-2ee8eaaf4900")
        output = out.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_all_correct(self):
        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900)}
        testmodel = BaseModel(test_args)
        testmodel.save()
        with captured_output() as (out, err):
            self.cli.do_all("")
        output = out.getvalue().strip()
        self.assertFalse("123-456-abc" in output)

    def test_all_error_invalid_class(self):
        with captured_output() as (out, err):
            self.cli.do_all("Human")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")
        with captured_output() as (out, err):
            self.cli.do_show("BaseModel d3da85f2-499c-43cb-b33d-3d7935bc808c")
        output = out.getvalue().strip()
        self.assertFalse("Ace" in output)

    def test_update_error_invalid_id(self):
        with captured_output() as (out, err):
            self.cli.do_update("BaseModel 123-456-abcic name Cat")
        output = out.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_update_error_invalid_class(self):
        with captured_output() as (out, err):
            self.cli.do_update("Human " +
                               "d3da85f2-499c-43cb-b33d-3d7935bc808c name Cat")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_error_missing_value(self):
        with captured_output() as (out, err):
            self.cli.do_update("BaseModel " +
                               "d3da85f2-499c-43cb-b33d-3d7935bc808c name")
        output = out.getvalue().strip()
        self.assertEqual(output, "** value missing **")


if __name__ == "__main__":
    unittest.main()
