#!/usr/bin/env python3
"""Unit and integration tests for client.py"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class, parameterized
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from client import GithubOrgClient

@parameterized_class("org_payload", org_payload)
class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method"""
        mock_get_json.return_value = self.org_payload
        github_client = GithubOrgClient(org_name)
        org_info = github_client.org()
        self.assertEqual(org_info, self.org_payload)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=property)
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url property"""
        mock_org.return_value = self.org_payload
        github_client = GithubOrgClient("testorg")
        self.assertEqual(github_client._public_repos_url, self.org_payload.get('repos_url'))

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=property)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test public_repos method"""
        mock_public_repos_url.return_value = "https://api.github.com/orgs/testorg/repos"
        mock_get_json.return_value = repos_payload
        github_client = GithubOrgClient("testorg")
        repos = github_client.public_repos()
        self.assertEqual(repos, expected_repos)
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/testorg/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_has_license):
        """Test has_license method"""
        github_client = GithubOrgClient("testorg")
        has_license = github_client.has_license(repo, license_key)
        self.assertEqual(has_license, expected_has_license)

@parameterized_class("org_payload", org_payload)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Set up class for integration tests"""
        cls.get_patcher = patch('client.get_json')
        cls.mock_get_json = cls.get_patcher.start()
        cls.mock_get_json.side_effect = [
            cls.org_payload,
            repos_payload,
            repos_payload,
            repos_payload,
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down class for integration tests"""
        cls.get_patcher.stop()

    def test_integration_public_repos(self):
        """Integration test for public_repos method"""
        org_name = self.org_payload.get('login')
        github_client = GithubOrgClient(org_name)
        repos = github_client.public_repos(license="apache-2.0")
        self.assertEqual(repos, apache2_repos)

    def test_public_repos(self):
        """Integration test for public_repos method using fixtures"""
        org_name = self.org_payload.get('login')
        github_client = GithubOrgClient(org_name)
        repos = github_client.public_repos()
        self.assertEqual(repos, expected_repos)

    def test_public_repos_with_license(self):
        """Integration test for public_repos method with license argument using fixtures"""
        org_name = self.org_payload.get('login')
        github_client = GithubOrgClient(org_name)
        repos = github_client.public_repos(license="apache-2.0")
        self.assertEqual(repos, apache2_repos)

if __name__ == "__main__":
    unittest.main()
