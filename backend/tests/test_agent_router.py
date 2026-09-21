from app.agent.router import AgentRouter
def test_routes():
 r=AgentRouter(); assert r.route('write a Ship 30 for 30 essay')=='ship30'; assert r.route('create an HTML artifact')=='artifact'; assert r.route('how do I improve onboarding?')=='qa'
