#!/usr/bin/env python3
"""Unit tests for client.py"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org method"""
        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        result = client.org()

        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/" + org_name)
        self.assertEqual(result, test_payload)

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url property"""
        test_payload = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"}
        mock_org.return_value = test_payload

        client = GithubOrgClient("testorg")
        result = client._public_repos_url

        mock_org.assert_called_once()
        self.assertEqual(result, "https://api.github.com/orgs/testorg/repos")


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient class"""

    fixtures = __import__('fixtures')

    @classmethod
    def setUpClass(cls):
        """Set up the test class"""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

    @parameterized_class("org_payload", "repos_payload",
                         "expected_repos", "apache2_repos", fixtures)
    def test_public_repos(self, org_payload, repos_payload,
                          expected_repos, apache2_repos):
        """Integration test for GithubOrgClient.public_repos"""
        org_name = org_payload["login"]
        self.mock_get.return_value.json.side_effect = [org_payload,
                                                       repos_payload]

        client = GithubOrgClient(org_name)
        result = client.public_repos()

        self.assertEqual(result, expected_repos)
        self.mock_get.assert_called_once_with(org_payload["repos_url"])
        self.mock_get.reset_mock()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class"""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
