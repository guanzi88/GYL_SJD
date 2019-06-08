from businessView.bzqyj import Bzqyj
from businessView.cgd import Cgd
from businessView.dfh import Dfh
from businessView.dsh import Dsh
from businessView.dzhz import Dzhz
from businessView.kc import Kc
from businessView.kcyj import Kcyj
from businessView.pd import Pd
from businessView.purchase import Purchase
from businessView.shbb import Shbb
from businessView.sp_sgd import Sp_Sgd
from common.myunit import StartEnd
from businessView.loginView import LoginView
from businessView.logout import LogOut
from businessView.sgd import Sgd
import unittest
import time


class Test_all(StartEnd):
    csv_file = '../data/account.csv'

    # @unittest.skip
    def test_a_login(self):
        """登陆供应链商家端"""
        L = LoginView(self.driver)
        data = L.get_csv_data(self.csv_file,1)
        L.loginview(data[0],data[1])

    # @unittest.skip   #不执行该用例
    def test_b_purchase(self):
        """创建申购单"""
        P = Purchase(self.driver)
        P.purchase()
        time.sleep(2)

    # @unittest.skip
    def test_c_spsgd(self):
        """审批申购单"""
        SP = Sp_Sgd(self.driver)
        SP.sp_sgd()
        time.sleep(2)

    # @unittest.skip
    def test_d_sgd(self):
        """查看申购单及详情"""
        S = Sgd(self.driver)
        S.sgd()
        time.sleep(2)

    # @unittest.skip
    def test_e_cgd(self):
        """查看采购单及详情"""
        C = Cgd(self.driver)
        C.cgd()
        time.sleep(2)

    # @unittest.skip
    def test_f_logout(self):
        """退出供应链商家端"""
        L = LogOut(self.driver)
        L.logout()

    # @unittest.skip
    def test_g_login(self):
        """登陆供应链商家端"""
        L = LoginView(self.driver)
        data = L.get_csv_data(self.csv_file,2)
        L.loginview(data[0],data[1])

    # @unittest.skip
    def test_h_dfh(self):
        """集团发货"""
        D = Dfh(self.driver)
        D.dfh()

    # @unittest.skip
    def test_i_logout(self):
        """退出供应链商家端"""
        L = LogOut(self.driver)
        L.logout()

    # @unittest.skip
    def test_j_login(self):
        """登陆供应链商家端"""
        L = LoginView(self.driver)
        data = L.get_csv_data(self.csv_file,1)
        L.loginview(data[0],data[1])

    # @unittest.skip
    def test_k_dsh(self):
        """门店收货"""
        D = Dsh(self.driver)
        D.dsh()

    # @unittest.skip
    def test_l_Pd(self):
        """盘点"""
        P = Pd(self.driver)
        P.pd()

    # @unittest.skip
    def test_m_bzqyj(self):
        """库存查询"""
        K = Kc(self.driver)
        K.kc()
    # @unittest.skip
    def test_n_Pd(self):
        """保质期预警"""
        B = Bzqyj(self.driver)
        B.bzqyj()

    # @unittest.skip
    def test_o_Pd(self):
        """库存预警"""
        K = Kcyj(self.driver)
        K.kcyj()

    # @unittest.skip
    def test_p_Pd(self):
        """收货报表"""
        S = Shbb(self.driver)
        S.shbb()

    # @unittest.skip
    def test_r_dzhz(self):
        """对账汇总"""
        D = Dzhz(self.driver)
        D.dzhz()

    # @unittest.skip
    def test_z_logout(self):
        """退出供应链商家端"""
        L = LogOut(self.driver)
        L.logout()

if __name__ == '__main__':
    unittest.main()