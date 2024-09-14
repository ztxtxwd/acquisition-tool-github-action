import unittest
from unittest.mock import patch, mock_open
import os
from download_and_compare import download_webpage, save_webpage, compare_and_save

class TestWebpageMonitor(unittest.TestCase):

    @patch('requests.get')
    def test_download_webpage(self, mock_get):
        mock_get.return_value.text = "测试网页内容"
        content = download_webpage()
        self.assertEqual(content, "测试网页内容")

    @patch('os.path.exists')
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_webpage(self, mock_file, mock_makedirs, mock_exists):
        mock_exists.return_value = False
        filename = save_webpage("测试网页内容")
        self.assertTrue(filename.startswith("webpage_"))
        self.assertTrue(filename.endswith(".html"))
        mock_file().write.assert_called_once_with("测试网页内容")

    @patch('download_and_compare.download_webpage')
    @patch('download_and_compare.save_webpage')
    @patch('os.listdir')
    @patch('builtins.open', new_callable=mock_open)
    def test_compare_and_save(self, mock_file, mock_listdir, mock_save, mock_download):
        # 模拟首次下载
        mock_listdir.return_value = []
        mock_download.return_value = "新网页内容"
        mock_save.return_value = "webpage_20230101_000000.html"

        with patch('builtins.print') as mock_print:
            compare_and_save()
            mock_print.assert_called_with("首次下载。已保存为 webpage_20230101_000000.html")

        # 模拟检测到变化
        mock_listdir.return_value = ["webpage_20230101_000000.html"]
        mock_file().read.return_value = "旧网页内容"
        mock_download.return_value = "新网页内容"
        mock_save.return_value = "webpage_20230101_010000.html"

        with patch('builtins.print') as mock_print:
            compare_and_save()
            mock_print.assert_called_with("检测到变化。已保存为 webpage_20230101_010000.html")

        # 模拟未检测到变化
        mock_file().read.return_value = "相同内容"
        mock_download.return_value = "相同内容"

        with patch('builtins.print') as mock_print:
            compare_and_save()
            mock_print.assert_called_with("未检测到变化。")

if __name__ == '__main__':
    unittest.main()