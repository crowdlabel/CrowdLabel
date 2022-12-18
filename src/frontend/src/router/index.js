import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ReceiverLogin from '../views/ReceiverLogin.vue'
import SenderLogin from '../views/SenderLogin.vue'
import ProjectsHallView from '../views/ProjectsHallView.vue'
import HistoryView from '../views/HistoryView.vue'
import CreditsView from '../views/CreditsView.vue'
import DraftBoxView from '../views/DraftBoxView.vue'
import MyAccountView from '../views/MyAccountView.vue'
import EditMyAccountView from '../views/EditMyAccountView.vue'
import NotificationsView from '../views/NotificationsView.vue'
import ProjectDetailView from '../views/ProjectDetailView'
import QuestionAudio from '../views/QuestionAudio.vue'
import QuestionText from '../views/QuestionText.vue'
import QuestionImageClassify from '../views/QuestionImageClassify.vue'
import QuestionImageIdentify from '../views/QuestionImageIdentify.vue'
import MissionComplete from '../views/MissionComplete.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import SenderHome from '../views/SenderHome.vue'
import SenderCredits from '../views/SenderCredits.vue'
import SenderMission from '../views/SenderMission.vue'

Vue.use(VueRouter)
Vue.use(VueAxios, axios)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/receiverlogin',
    name: 'receiverlogin',
    component: ReceiverLogin
  },
  {
    path: '/senderlogin',
    name: 'senderlogin',
    component: SenderLogin
  },
  {
    path: '/projects',
    name: 'projects',
    component: ProjectsHallView
  },
  {
    path: '/history',
    name: 'history',
    component: HistoryView
  },
  {
    path: '/credits',
    name: 'credits',
    component: CreditsView
  },
  {
    path: '/draftbox',
    name: 'draftbox',
    component: DraftBoxView
  },
  {
    path: '/myaccount',
    name: 'myaccount',
    component: MyAccountView
  },
  {
    path: '/editmyaccount',
    name: 'editmyaccount',
    component: EditMyAccountView
  },
  {
    path: '/notifications',
    name: 'notifications',
    component: NotificationsView
  },
  {
    path: '/project_detail',
    name: 'project_detail',
    component: ProjectDetailView
  },
  {
    path: '/question_text',
    name: 'question_text',
    component: QuestionText
  },
  {
    path: '/question_audio',
    name: 'question_audio',
    component: QuestionAudio
  },
  {
    path: '/question_image_classify',
    name: 'question_image_classify',
    component: QuestionImageClassify
  },
  {
    path: '/question_image_identify',
    name: 'question_image_identify',
    component: QuestionImageIdentify
  },
  {
    path: '/mission_complete',
    name: 'mission_complete',
    component: MissionComplete
  },
  {
    path: '/senderhome',
    name: 'senderhome',
    component: SenderHome,
    redirect:'/sendermission',
  },
  {
    path: '/sendermission',
    name:'sendermission',
    component: SenderMission
  },
  {
    path: '/sendercredits',
    name:'sendercredits',
    component: SenderCredits
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
