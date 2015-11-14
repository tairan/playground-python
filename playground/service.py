
import datetime
import pytz

from .models import (
	Account
)


class AccountService():
	def __init__(self, session):
		self.session = session

	def sign_in(self, name):
		user = self.session.Query(Account).filter(name=name).fisrt()
		if user:
			user.last_signed_at = datetime.datetime.now(datetime.datetime.now(tz=pytz.timezone('UTC')))
		else:
			raise Exception('user `{0}` does not exist.'.format(name))
			
			
	def create_new_user(self, name):
		if not self.user_exists(name):
			act = Account(name=name)
			self.session.add(act)
			act.commit()
			return act
		else:
			raise Exception('user `{0}` already exist.'.format(name))
		
		
	def user_exists(self, name):
		account = self.session.query(Account).filter_by(name = name).first()
		return account != null
	
