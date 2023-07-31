#!/usr/bin/env python3
"""Unit tests for client.py"""

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized_class
from client import GithubOrgClient

@parameterized_class("org_payload", "repos_payload", "expected_repos", "apache2_repos", [
    ({"login": "google"}, [{"name": "repo1"}, {"name": "repo2"}], ["repo1", "repo2"], ["repo1"]),
    ({"login": "abc"}, [{"name": "repo3"}, {"name": "repo4"}], ["repo3", "repo4"], []),
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class for integration test"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class after integration test"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method of GithubOrgClient"""
        self.mock_get.return_value.json.side_effect = [self.org_payload, self.repos_payload]

        github_client = GithubOrgClient(self.org_payload["login"])
        repos = github_client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method of GithubOrgClient with a specific license"""
        self.mock_get.return_value.json.side_effect = [self.org_payload, self.repos_payload]

        github_client = GithubOrgClient(self.org_payload["login"])
        repos_with_license = github_client.public_repos(license="apache-2.0")
        self.assertEqual(repos_with_license, self.apache2_repos)

if __name__ == "__main__":
    unittest.main()
