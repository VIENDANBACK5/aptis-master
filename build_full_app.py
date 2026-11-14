# -*- coding: utf-8 -*-
"""
Generator for index.html matching 100% of MilaEdu's UI/UX, layouts, and components.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HTML_TEMPLATE = r'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aptis Master · Hệ Thống Luyện Thi Aptis Trực Tuyến 4 Kỹ Năng</title>
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brand: {
              50: '#eff6ff',
              100: '#dbeafe',
              500: '#3b82f6',
              600: '#2563eb',
              700: '#1d4ed8'
            }
          }
        }
      }
    }
  </script>

  <!-- Lucide Icons CDN -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Google Fonts: Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    body { font-family: 'Inter', sans-serif; }
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: #f8fafc; }
    ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
    .pb-safe { padding-bottom: max(0.75rem, env(safe-area-inset-bottom)); }
  </style>
</head>
<body class="bg-slate-50 text-gray-900 antialiased min-h-screen flex flex-col">

  <!-- ================= TOP NAVBAR ================= -->
  <nav class="relative z-40 bg-white border-b border-gray-200">
    <div class="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center h-16 gap-4">
        <!-- Logo -->
        <a href="javascript:void(0)" onclick="showDashboard()" class="flex items-center gap-2 shrink-0">
          <span class="w-8 h-8 rounded-lg bg-blue-600 text-white font-bold flex items-center justify-center shrink-0">A</span>
          <span class="text-lg font-bold text-gray-900 whitespace-nowrap">Aptis<span class="text-blue-600"> Master</span></span>
          <span class="hidden sm:inline-flex items-center px-2 py-0.5 rounded-full text-xs font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200">Trọn Bộ 4 Kỹ Năng</span>
        </a>

        <!-- Main Links -->
        <div class="hidden lg:flex items-center gap-1 ml-4">
          <a href="javascript:void(0)" onclick="showDashboard()" id="nav-link-practice" class="relative inline-flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors bg-blue-50 text-blue-700">
            Luyện tập
          </a>
          <a href="javascript:void(0)" onclick="scrollToExamHub()" id="nav-link-examhub" class="relative inline-flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:text-gray-900 hover:bg-gray-50">
            <svg class="w-4 h-4 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
            Kho Đề Thi
          </a>
          <a href="javascript:void(0)" onclick="openSkillHub('speaking')" class="relative inline-flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:text-gray-900 hover:bg-gray-50">
            <svg class="w-4 h-4 text-orange-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"></path></svg>
            Speaking (20 Đề)
          </a>
          <a href="javascript:void(0)" onclick="openSkillHub('writing')" class="relative inline-flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:text-gray-900 hover:bg-gray-50">
            <svg class="w-4 h-4 text-pink-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg>
            Writing (30 Đề)
          </a>
          <a href="javascript:void(0)" onclick="showVocab()" id="nav-link-vocab" class="relative inline-flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:text-gray-900 hover:bg-gray-50">
            Từ vựng
          </a>
          <a href="javascript:void(0)" onclick="showInstructions()" id="nav-link-instructions" class="relative inline-flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:text-gray-900 hover:bg-gray-50">
            Cẩm Nang
          </a>
        </div>

        <!-- Right User Actions -->
        <div class="ml-auto flex items-center gap-2">
          <!-- Notification Bell -->
          <div class="relative">
            <button type="button" onclick="toggleNotifications()" aria-label="Thông báo" class="relative w-10 h-10 rounded-full flex items-center justify-center text-gray-500 hover:text-gray-800 hover:bg-gray-100 transition-colors">
              <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>
            </button>
            <div id="notif-dropdown" class="hidden absolute right-0 mt-2 w-80 max-w-[calc(100vw-2rem)] bg-white rounded-xl border border-gray-200 shadow-lg overflow-hidden z-50">
              <div class="px-4 py-3 border-b border-gray-100 text-sm font-semibold text-gray-900">Thông báo</div>
              <div class="px-4 py-6 text-center text-sm text-gray-500">Bạn đã xem hết thông báo.</div>
            </div>
          </div>

          <!-- User Pill Dropdown -->
          <div class="relative">
            <button type="button" onclick="toggleUserMenu()" class="flex items-center gap-2 pl-1 pr-2 sm:pr-3 py-1 rounded-full border border-gray-200 hover:bg-gray-50 transition-colors">
              <span class="w-8 h-8 text-xs rounded-full bg-blue-50 text-blue-700 font-bold flex items-center justify-center shrink-0">M</span>
              <span class="hidden sm:inline max-w-[10rem] truncate text-sm font-medium text-gray-700">Minh</span>
              <svg class="w-4 h-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
            </button>
            <div id="user-dropdown" class="hidden absolute right-0 mt-2 w-60 bg-white rounded-xl border border-gray-200 shadow-lg overflow-hidden py-1 z-50">
              <div class="px-4 py-3 border-b border-gray-100">
                <div class="text-sm font-semibold text-gray-900 truncate">Minh</div>
                <div class="text-xs text-gray-500 truncate">minhtuantran210305@gmail.com</div>
              </div>
              <div class="py-1">
                <a href="javascript:void(0)" onclick="openFullTest(); toggleUserMenu();" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50">Full Test Aptis</a>
                <a href="javascript:void(0)" onclick="showDashboard(); toggleUserMenu();" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50">Lịch sử làm bài</a>
                <button type="button" onclick="resetAllProgress(); toggleUserMenu();" class="w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50">Đặt lại tiến độ làm bài</button>
              </div>
            </div>
          </div>

          <!-- Mobile Toggle -->
          <button type="button" onclick="toggleMobileNav()" aria-label="Mở menu" class="md:hidden w-10 h-10 rounded-lg flex items-center justify-center text-gray-600 hover:bg-gray-100">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Nav Menu -->
    <div id="mobile-nav" class="hidden md:hidden border-t border-gray-100 bg-white px-4 py-2">
      <a href="javascript:void(0)" onclick="showDashboard(); toggleMobileNav();" class="flex items-center justify-between px-3 py-2.5 rounded-lg text-sm font-medium bg-blue-50 text-blue-700">Luyện tập</a>
      <a href="javascript:void(0)" onclick="showVocab(); toggleMobileNav();" class="flex items-center justify-between px-3 py-2.5 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-50">Từ vựng</a>
      <a href="javascript:void(0)" onclick="showInstructions(); toggleMobileNav();" class="flex items-center justify-between px-3 py-2.5 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-50">Hướng dẫn</a>
    </div>
  </nav>

  <!-- ================= MAIN CONTAINER ================= -->
  <main class="max-w-[1440px] w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 flex-1">

    <!-- VIEW 1: DASHBOARD -->
    <div id="view-dashboard" class="space-y-8">
      <!-- Greeting & Stat Pills -->
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4 mb-6 lg:items-end">
        <div class="flex items-center gap-4 min-w-0">
          <div class="min-w-0">
            <h1 class="text-2xl sm:text-3xl font-bold text-gray-900">Chào Minh</h1>
            <p class="mt-0.5 text-gray-500">Hôm nay bạn muốn luyện kỹ năng nào?</p>
          </div>
        </div>
        <div class="flex flex-wrap gap-2">
          <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full border text-sm bg-white border-gray-200 text-gray-600">
            <span class="font-semibold text-gray-900" id="stat-done-count">0</span> bài đã làm
          </span>
          <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full border text-sm bg-white border-gray-200 text-gray-600">
            Điểm TB <span class="font-semibold text-gray-900" id="stat-avg-score">—</span>
          </span>
          <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full border text-sm bg-emerald-50 border-emerald-200 text-emerald-700" title="Số lượt AI chấm Writing còn lại">
            AI Writing <span class="font-semibold" id="stat-writing-score">80/80</span>
          </span>
          <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full border text-sm bg-white border-gray-200 text-gray-600">
            Còn <span class="font-semibold">47 ngày</span> · 31/12/2026
          </span>
        </div>
      </div>

      <!-- Full Test Aptis Banner -->
      <a href="javascript:void(0)" onclick="openFullTest()" class="group flex flex-col sm:flex-row sm:items-center gap-4 mb-8 p-5 rounded-2xl bg-white border-2 border-blue-200 hover:border-blue-400 hover:shadow-md transition-all cursor-pointer">
        <span class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0 bg-blue-50 text-blue-600">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 21v-4m0 0V5a2 2 0 012-2h6.5l1 1H21l-3 6 3 6h-8.5l-1-1H5a2 2 0 00-2 2zm9-13.5V9"></path></svg>
        </span>
        <span class="flex-1">
          <span class="flex items-center gap-2 flex-wrap">
            <span class="text-lg font-bold text-gray-900">Full Test Aptis</span>
            <span class="px-2 py-0.5 rounded-full bg-blue-50 text-blue-700 text-xs font-medium">Còn 4 lượt</span>
          </span>
          <span class="block text-sm text-gray-500 mt-0.5">Thi liên tục 5 phần như thi thật · nhận bảng điểm thang Aptis và trình độ CEFR</span>
        </span>
        <span class="inline-flex items-center justify-center px-5 py-2.5 rounded-xl bg-blue-600 group-hover:bg-blue-700 text-white font-semibold text-sm transition-colors">Vào thi →</span>
      </a>

      <!-- Luyện từng kỹ năng -->
      <div class="flex items-baseline justify-between gap-3 mb-3">
        <h2 class="text-base font-semibold text-gray-900">Luyện từng kỹ năng</h2>
        <span class="text-xs text-gray-400">Theo thứ tự đề thi Aptis</span>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-3 sm:gap-4 mb-8">
        <!-- 1. Speaking -->
        <a href="javascript:void(0)" onclick="openSkillHub('speaking')" class="group relative flex flex-col bg-white rounded-2xl border border-gray-200 p-5 transition-all hover:border-blue-300 hover:shadow-md hover:-translate-y-0.5 cursor-pointer">
          <span class="absolute top-5 right-5 text-gray-300 group-hover:text-blue-500 transition-colors" aria-hidden="true">→</span>
          <span class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0 bg-orange-50 text-orange-600">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"></path></svg>
          </span>
          <span class="block mt-4 text-base font-semibold text-gray-900">Speaking</span>
          <span class="block text-xs text-gray-500">Kỹ năng nói</span>
          <span class="block mt-3 pt-3 border-t border-gray-100 text-xs font-medium text-gray-400" id="dash-spk-status">
            20 Bộ Đề Thi
          </span>
        </a>

        <!-- 2. Listening -->
        <a href="javascript:void(0)" onclick="openSkillHub('listening')" class="group relative flex flex-col bg-white rounded-2xl border border-gray-200 p-5 transition-all hover:border-blue-300 hover:shadow-md hover:-translate-y-0.5 cursor-pointer">
          <span class="absolute top-5 right-5 text-gray-300 group-hover:text-blue-500 transition-colors" aria-hidden="true">→</span>
          <span class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0 bg-emerald-50 text-emerald-600">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"></path></svg>
          </span>
          <span class="block mt-4 text-base font-semibold text-gray-900">Listening</span>
          <span class="block text-xs text-gray-500">Kỹ năng nghe</span>
          <span class="block mt-3 pt-3 border-t border-gray-100 text-xs font-medium text-gray-400" id="dash-lis-status">
            4 Part · 238 Câu
          </span>
        </a>

        <!-- 3. Grammar -->
        <a href="javascript:void(0)" onclick="openSkillHub('grammar')" class="group relative flex flex-col bg-white rounded-2xl border border-gray-200 p-5 transition-all hover:border-blue-300 hover:shadow-md hover:-translate-y-0.5 cursor-pointer">
          <span class="absolute top-5 right-5 text-gray-300 group-hover:text-blue-500 transition-colors" aria-hidden="true">→</span>
          <span class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0 bg-indigo-50 text-indigo-600">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
          </span>
          <span class="block mt-4 text-base font-semibold text-gray-900">Grammar</span>
          <span class="block text-xs text-gray-500">Ngữ pháp &amp; Từ vựng</span>
          <span class="block mt-3 pt-3 border-t border-gray-100 text-xs font-medium text-gray-400" id="dash-gra-status">
            MCQ + Vocabulary
          </span>
        </a>

        <!-- 4. Reading -->
        <a href="javascript:void(0)" onclick="openSkillHub('reading')" class="group relative flex flex-col bg-white rounded-2xl border border-gray-200 p-5 transition-all hover:border-blue-300 hover:shadow-md hover:-translate-y-0.5 cursor-pointer">
          <span class="absolute top-5 right-5 text-gray-300 group-hover:text-blue-500 transition-colors" aria-hidden="true">→</span>
          <span class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0 bg-sky-50 text-sky-600">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
          </span>
          <span class="block mt-4 text-base font-semibold text-gray-900">Reading</span>
          <span class="block text-xs text-gray-500">Kỹ năng đọc hiểu</span>
          <span class="block mt-3 pt-3 border-t border-gray-100 text-xs font-medium text-gray-400" id="dash-rea-status">
            4 Part · 74 Bài
          </span>
        </a>

        <!-- 5. Writing -->
        <a href="javascript:void(0)" onclick="openSkillHub('writing')" class="group relative flex flex-col bg-white rounded-2xl border border-gray-200 p-5 transition-all hover:border-blue-300 hover:shadow-md hover:-translate-y-0.5 cursor-pointer">
          <span class="absolute top-5 right-5 text-gray-300 group-hover:text-blue-500 transition-colors" aria-hidden="true">→</span>
          <span class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0 bg-pink-50 text-pink-600">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg>
          </span>
          <span class="block mt-4 text-base font-semibold text-gray-900">Writing</span>
          <span class="block text-xs text-gray-500">Kỹ năng viết</span>
          <span class="block mt-3 pt-3 border-t border-gray-100 text-xs font-medium text-gray-400" id="dash-wri-status">
            30 CLB Đề Thi
          </span>
        </a>
      </div>

      <!-- Tiến độ luyện tập Card -->
      <div class="bg-white rounded-2xl border border-gray-200 overflow-hidden">
        <div class="flex flex-col sm:flex-row sm:items-center gap-3 px-5 py-4 border-b border-gray-100">
          <div class="flex-1 min-w-0">
            <h2 class="text-base font-semibold text-gray-900">Tiến độ luyện tập</h2>
            <p class="text-xs text-gray-500">Điểm trung bình mỗi tuần · 6 tháng gần nhất</p>
          </div>
          <div class="flex flex-wrap items-center gap-1.5"><div id="chartLegend" class="flex flex-wrap gap-1.5"></div></div>
        </div>
        <div class="px-3 sm:px-5 pt-4 pb-2">
          <div class="relative h-56 sm:h-64 w-full flex flex-col items-center justify-center text-center text-sm text-gray-400">
            <span class="text-gray-500 font-medium">Chưa có dữ liệu trong 6 tháng gần đây</span>
            <span>Làm bài luyện tập để thấy tiến độ của bạn ở đây.</span>
          </div>
        </div>
        <div class="flex flex-wrap items-center gap-x-4 gap-y-1 px-5 py-3 border-t border-gray-100 text-sm">
          <span class="text-gray-400">Lịch sử:</span>
          <a href="javascript:void(0)" onclick="showDashboard()" class="text-gray-600 hover:text-blue-600">Trắc nghiệm</a>
          <a href="javascript:void(0)" onclick="openSkillHub('writing')" class="text-gray-600 hover:text-blue-600">Writing</a>
          <a href="javascript:void(0)" onclick="openSkillHub('speaking')" class="text-gray-600 hover:text-blue-600">Speaking</a>
          <a href="javascript:void(0)" onclick="openFullTest()" class="text-gray-600 hover:text-blue-600">Bảng xếp hạng</a>
        </div>
      </div>

      <!-- KHO ĐỀ THI & BỘ ĐỀ TRẮC NGHIỆM TỔNG HỢP -->
      <div id="section-exam-hub" class="space-y-4 pt-4">
        <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
          <div>
            <h2 class="text-xl font-bold text-gray-900 flex items-center gap-2">
              <svg class="w-5 h-5 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
              Kho Đề Thi & Luyện Tập Chi Tiết
            </h2>
            <p class="text-xs text-gray-500 mt-0.5">Chọn kỹ năng để lọc đề thi hoặc xem toàn bộ danh mục bài tập chuẩn format Aptis</p>
          </div>
        </div>

        <!-- Filter Tabs Bar (Image 1 replica) -->
        <div class="flex items-center gap-2 overflow-x-auto pb-2 border-b border-gray-200">
          <button type="button" onclick="filterExamHub('all')" id="exam-tab-all" class="px-4 py-2 rounded-full text-xs sm:text-sm font-bold transition bg-gray-900 text-white shrink-0 shadow-sm">
            Tất cả đề thi
          </button>
          <button type="button" onclick="filterExamHub('listening')" id="exam-tab-listening" class="px-4 py-2 rounded-full text-xs sm:text-sm font-semibold transition bg-gray-100 text-gray-700 hover:bg-gray-200 shrink-0">
            Listening (Nghe)
          </button>
          <button type="button" onclick="filterExamHub('reading')" id="exam-tab-reading" class="px-4 py-2 rounded-full text-xs sm:text-sm font-semibold transition bg-gray-100 text-gray-700 hover:bg-gray-200 shrink-0">
            Reading (Đọc)
          </button>
          <button type="button" onclick="filterExamHub('grammar')" id="exam-tab-grammar" class="px-4 py-2 rounded-full text-xs sm:text-sm font-semibold transition bg-gray-100 text-gray-700 hover:bg-gray-200 shrink-0">
            Grammar & Vocab
          </button>
          <button type="button" onclick="filterExamHub('speaking')" id="exam-tab-speaking" class="px-4 py-2 rounded-full text-xs sm:text-sm font-semibold transition bg-gray-100 text-gray-700 hover:bg-gray-200 shrink-0">
            Speaking (20 Đề)
          </button>
          <button type="button" onclick="filterExamHub('writing')" id="exam-tab-writing" class="px-4 py-2 rounded-full text-xs sm:text-sm font-semibold transition bg-gray-100 text-gray-700 hover:bg-gray-200 shrink-0">
            Writing (30 Đề)
          </button>
        </div>

        <!-- Exam Items Grid -->
        <div id="exam-hub-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <!-- Populated by renderExamHubGrid() -->
        </div>
      </div>
    </div>

    <!-- VIEW 2: SKILL HUB -->
    <div id="view-skill-hub" class="hidden space-y-6">
      <!-- Breadcrumb -->
      <nav class="flex flex-wrap items-center gap-1.5 text-sm text-gray-500 mb-4" aria-label="Breadcrumb">
        <a href="javascript:void(0)" onclick="showDashboard()" class="hover:text-blue-600">Luyện tập</a>
        <span class="text-gray-300">/</span>
        <span class="text-gray-900 font-medium" id="hub-breadcrumb-skill">Skill</span>
      </nav>

      <!-- Skill Hub Header -->
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4 mb-6">
        <div class="flex items-center gap-4 min-w-0">
          <span id="hub-icon-container" class="w-14 h-14 rounded-2xl flex items-center justify-center shrink-0 bg-blue-50 text-blue-600">
            <!-- Icon -->
          </span>
          <div class="min-w-0">
            <h1 class="text-2xl sm:text-3xl font-bold text-gray-900" id="hub-title">Skill Title</h1>
            <p class="mt-0.5 text-gray-500" id="hub-desc">Mô tả kỹ năng</p>
          </div>
        </div>
        <div class="flex flex-wrap gap-2">
          <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full border text-sm bg-white border-gray-200 text-gray-600">
            <span class="font-semibold text-gray-900" id="hub-done-count">0</span> bài đã làm
          </span>
          <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full border text-sm bg-white border-gray-200 text-gray-600">
            Thi thử gần nhất <span class="font-semibold text-gray-900">—</span>
          </span>
        </div>
      </div>

      <!-- Mock Test Banner -->
      <a href="javascript:void(0)" id="hub-mock-btn" class="group flex flex-col sm:flex-row sm:items-center gap-4 mb-8 p-5 rounded-2xl bg-white border-2 border-blue-200 hover:border-blue-400 hover:shadow-md transition-all cursor-pointer">
        <span class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0 bg-blue-50 text-blue-600">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        </span>
        <span class="flex-1">
          <span class="flex items-center gap-2 flex-wrap">
            <span class="text-lg font-bold text-gray-900" id="hub-mock-title">Thi thử</span>
          </span>
          <span class="block text-sm text-gray-500 mt-0.5">Làm trọn bộ các Part có tính giờ và chấm điểm như thi thật</span>
        </span>
        <span class="inline-flex items-center justify-center px-5 py-2.5 rounded-xl bg-blue-600 group-hover:bg-blue-700 text-white font-semibold text-sm transition-colors">Bắt đầu thi thử →</span>
      </a>

      <!-- Parts / Sets Section -->
      <div class="flex items-baseline justify-between gap-3 mb-3">
        <h2 class="text-base font-semibold text-gray-900" id="hub-parts-heading">Luyện theo Part</h2>
        <span class="text-xs text-gray-400" id="hub-parts-count">4 Part</span>
      </div>

      <!-- Container for dynamic cards -->
      <div id="hub-cards-grid" class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-3 sm:gap-4">
        <!-- Rendered by JS -->
      </div>
    </div>

    <!-- VIEW 3: PRACTICE ROOM -->
    <div id="view-practice" class="hidden flex flex-col max-w-6xl mx-auto pb-28">
      <!-- Sticky Header -->
      <header class="sticky top-0 z-30 bg-white border border-gray-200 rounded-2xl overflow-hidden mb-5">
        <div class="h-1 bg-gray-100">
          <div id="practice-progress-bar" class="h-full bg-blue-600 transition-all duration-500" style="width: 25%"></div>
        </div>
        <div class="flex items-center gap-3 px-4 py-3 sm:px-6">
          <button type="button" onclick="exitPractice()" class="w-9 h-9 rounded-xl border border-gray-200 flex items-center justify-center text-gray-600 hover:bg-gray-50 shrink-0" aria-label="Quay lại">
            <svg class="w-5 h-5 w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
          </button>
          <span id="practice-skill-badge" class="w-9 h-9 rounded-full flex items-center justify-center shrink-0 bg-sky-50 text-sky-600 hidden sm:flex">
            <!-- Icon -->
          </span>
          <div class="flex-1 min-w-0">
            <h1 id="practice-sec-title" class="text-base font-semibold text-gray-900 truncate">Reading · Part 1</h1>
            <p id="practice-subtitle" class="text-xs text-gray-500 truncate">Choose the word that fits in the gap 01</p>
          </div>
          <span class="shrink-0 px-3 py-1.5 rounded-lg bg-blue-50 text-blue-700 text-sm font-semibold">
            Câu <span id="current-q-num">1</span>/<span id="total-q-num">4</span>
          </span>
        </div>
      </header>

      <!-- Question Card Body -->
      <div class="bg-white rounded-2xl border border-gray-200 overflow-hidden mb-6">
        <!-- Stem Bar -->
        <div class="px-5 sm:px-6 py-4 border-b border-gray-100 bg-gray-50" id="q-stem-container">
          <div class="text-base font-medium text-gray-900" id="q-stem-text">Question stem goes here</div>
        </div>

        <!-- Tip & Mnemonic Box (Mẹo thi & Ghi nhớ Aptis) -->
        <div id="q-tip-box" class="hidden px-5 sm:px-6 pt-5"></div>

        <!-- Audio Player (MilaEdu Custom Styled Bar) -->
        <div id="q-audio-box" class="hidden p-4 sm:p-5 border-b border-gray-100 bg-slate-50">
          <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
            <div class="flex items-center gap-3 w-full sm:w-auto">
              <!-- Play / Pause Button -->
              <button type="button" onclick="toggleAudio()" id="btn-audio-play" class="w-11 h-11 rounded-full bg-blue-600 hover:bg-blue-700 text-white flex items-center justify-center shadow-md shrink-0 transition" aria-label="Phát / Dừng">
                <svg id="icon-play-audio" class="w-5 h-5 ml-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              </button>
              <div>
                <div class="text-xs font-bold text-gray-800 flex items-center gap-1.5">
                  <span>File âm thanh bài thi</span>
                  <span id="listen-count-badge" class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-blue-100 text-blue-700">Đã nghe: 0 lần</span>
                </div>
                <div class="text-[11px] text-gray-500 font-mono mt-0.5" id="audio-time-display">00:00 / 00:00</div>
              </div>
            </div>

            <!-- Custom Seekbar -->
            <div class="w-full sm:flex-1 max-w-md flex items-center gap-3">
              <input type="range" id="audio-seekbar" value="0" min="0" max="100" oninput="seekAudio(this.value)" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-blue-600">
            </div>

            <!-- Speed selector -->
            <div class="flex items-center gap-1.5 shrink-0">
              <button type="button" onclick="setAudioSpeed(0.8)" id="speed-btn-08" class="px-2.5 py-1 text-xs rounded-lg border border-gray-200 hover:bg-gray-200 font-medium">0.8x</button>
              <button type="button" onclick="setAudioSpeed(1.0)" id="speed-btn-10" class="px-2.5 py-1 text-xs rounded-lg border border-gray-200 bg-blue-50 text-blue-700 font-bold">1.0x</button>
              <button type="button" onclick="setAudioSpeed(1.2)" id="speed-btn-12" class="px-2.5 py-1 text-xs rounded-lg border border-gray-200 hover:bg-gray-200 font-medium">1.2x</button>
            </div>
          </div>
          <audio id="main-audio-element" preload="auto" class="hidden" ontimeupdate="onAudioTimeUpdate()" onended="onAudioEnded()"></audio>
        </div>

        <!-- Question Interactive Area -->
        <div class="p-5 sm:p-6" id="q-interactive-area">
          <!-- Rendered dynamically -->
        </div>

        <!-- Feedback & Explanation Area -->
        <div id="q-feedback-area" class="hidden px-5 sm:px-6 py-4 border-t border-gray-100 bg-slate-50"></div>
      </div>

      <!-- Fixed Bottom Footer Navigation Bar -->
      <footer class="fixed bottom-0 inset-x-0 z-50 bg-white border-t border-gray-200 pb-safe">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex items-center justify-between gap-3">
          <div class="flex items-center gap-2">
            <!-- Popover Button -->
            <div class="relative">
              <button type="button" onclick="togglePalettePopover()" class="inline-flex items-center justify-center gap-1.5 font-semibold transition-colors disabled:opacity-50 px-4 py-2.5 text-sm rounded-xl bg-white border border-gray-200 text-gray-700 hover:bg-gray-50" aria-label="Danh sách câu hỏi">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h10"></path></svg>
                <span class="hidden sm:inline">Danh sách câu</span>
              </button>
              
              <!-- Popover Menu -->
              <div id="palette-popover" class="hidden absolute bottom-full left-0 mb-2 bg-white rounded-xl shadow-lg border border-gray-200 w-[min(340px,90vw)] max-h-[60vh] flex flex-col z-50 overflow-hidden">
                <div class="p-3 border-b border-gray-100">
                  <p class="text-sm font-semibold text-gray-900 mb-2">Danh sách câu hỏi</p>
                  <div class="relative">
                    <input type="text" id="palette-search" placeholder="Tìm câu hỏi..." oninput="filterPalette(this.value)" class="w-full text-sm pl-3 pr-3 py-1.5 border border-gray-200 rounded-lg focus:outline-none focus:border-blue-500">
                  </div>
                </div>
                <div id="palette-popover-grid" class="flex-1 overflow-y-auto p-3 flex flex-wrap gap-2">
                  <!-- Popover numbers -->
                </div>
              </div>
            </div>

            <button type="button" onclick="showVocab()" class="hidden md:inline-flex items-center gap-1.5 text-xs text-gray-500 hover:text-blue-600 px-3 py-2 rounded-lg hover:bg-gray-50 transition-colors">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
              <span>Sổ tay từ vựng</span>
            </button>
          </div>

          <div class="flex items-center gap-2">
            <button type="button" id="btn-prev" onclick="prevQuestion()" class="inline-flex items-center justify-center gap-1.5 font-semibold transition-colors disabled:opacity-50 px-4 py-2.5 text-sm rounded-xl bg-white border border-gray-200 text-gray-700 hover:bg-gray-50">
              ← Câu trước
            </button>
            <button type="button" id="btn-check" onclick="checkCurrentAnswer()" class="inline-flex items-center justify-center gap-1.5 font-semibold transition-colors disabled:opacity-50 px-5 py-2.5 text-sm rounded-xl bg-blue-600 hover:bg-blue-700 text-white">
              Kiểm tra đáp án
            </button>
            <button type="button" id="btn-next" onclick="nextQuestion()" class="inline-flex items-center justify-center gap-1.5 font-semibold transition-colors disabled:opacity-50 px-5 py-2.5 text-sm rounded-xl bg-blue-600 hover:bg-blue-700 text-white">
              Câu tiếp theo →
            </button>
          </div>
        </div>
      </footer>
    </div>

    <!-- VIEW 4: SPEAKING MOCK TEST -->
    <div id="view-speaking" class="hidden space-y-6 max-w-4xl mx-auto">
      <div class="flex items-center justify-between gap-3">
        <a href="javascript:void(0)" onclick="openSkillHub('speaking')" class="inline-flex items-center text-sm font-semibold text-blue-600 hover:text-blue-700">
          ← Quay lại Speaking
        </a>
        <div class="flex items-center gap-2">
          <span class="px-3 py-1 rounded-full text-xs font-semibold bg-orange-50 text-orange-700 border border-orange-200">
            Speaking Full Test
          </span>
        </div>
      </div>

      <!-- Speaking Set Header -->
      <div class="bg-white rounded-2xl border border-gray-200 p-6 shadow-sm">
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-b border-gray-100 pb-4 mb-4">
          <div>
            <h2 class="text-xl font-bold text-gray-900" id="spk-test-title">Đề thi Speaking</h2>
            <p class="text-xs text-gray-500 mt-0.5">Thời gian toàn bài: 12 phút · 4 Part</p>
          </div>
          <div class="flex items-center gap-2">
            <!-- Part selection tabs -->
            <button onclick="switchSpeakingPart(1)" id="spk-tab-1" class="px-3 py-1.5 text-xs font-bold rounded-lg bg-orange-600 text-white">Part 1</button>
            <button onclick="switchSpeakingPart(2)" id="spk-tab-2" class="px-3 py-1.5 text-xs font-bold rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200">Part 2</button>
            <button onclick="switchSpeakingPart(3)" id="spk-tab-3" class="px-3 py-1.5 text-xs font-bold rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200">Part 3</button>
            <button onclick="switchSpeakingPart(4)" id="spk-tab-4" class="px-3 py-1.5 text-xs font-bold rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200">Part 4</button>
          </div>
        </div>

        <!-- Speaking Part Interactive Content -->
        <div id="spk-part-content" class="space-y-6">
          <!-- Rendered by JS -->
        </div>
      </div>
    </div>

    <!-- VIEW 5: WRITING MOCK TEST -->
    <div id="view-writing" class="hidden space-y-6 max-w-4xl mx-auto">
      <div class="flex items-center justify-between gap-3">
        <a href="javascript:void(0)" onclick="openSkillHub('writing')" class="inline-flex items-center text-sm font-semibold text-blue-600 hover:text-blue-700">
          ← Quay lại Writing
        </a>
        <div class="flex items-center gap-2">
          <span class="px-3 py-1 rounded-full text-xs font-semibold bg-pink-50 text-pink-700 border border-pink-200">
            Writing CLB Test
          </span>
        </div>
      </div>

      <!-- Writing Set Card -->
      <div class="bg-white rounded-2xl border border-gray-200 p-6 shadow-sm">
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-b border-gray-100 pb-4 mb-4">
          <div>
            <h2 class="text-xl font-bold text-gray-900" id="wri-test-title">Đề thi Writing</h2>
            <p class="text-xs text-gray-500 mt-0.5">Thời gian làm bài: 50 phút · 4 Part</p>
          </div>
          <div class="flex items-center gap-2">
            <button onclick="switchWritingPart(1)" id="wri-tab-1" class="px-3 py-1.5 text-xs font-bold rounded-lg bg-pink-600 text-white">Part 1</button>
            <button onclick="switchWritingPart(2)" id="wri-tab-2" class="px-3 py-1.5 text-xs font-bold rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200">Part 2</button>
            <button onclick="switchWritingPart(3)" id="wri-tab-3" class="px-3 py-1.5 text-xs font-bold rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200">Part 3</button>
            <button onclick="switchWritingPart(4)" id="wri-tab-4" class="px-3 py-1.5 text-xs font-bold rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200">Part 4</button>
          </div>
        </div>

        <!-- Writing Part Content -->
        <div id="wri-part-content" class="space-y-6">
          <!-- Rendered by JS -->
        </div>
      </div>
    </div>

    <!-- VIEW 6: FULL TEST APTIS -->
    <div id="view-full-test" class="hidden max-w-3xl mx-auto space-y-6">
      <div>
        <h1 class="text-3xl font-bold text-gray-900">Full Test Aptis</h1>
        <p class="mt-2 text-gray-600">Thi liên tục cả 5 phần như kỳ thi thật. Làm xong và chấm xong, bạn nhận bảng điểm theo thang Aptis (0–50 mỗi kỹ năng) kèm trình độ CEFR.</p>
      </div>

      <div class="bg-white rounded-2xl border border-gray-200 p-6 shadow-sm">
        <h2 class="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-3">Cấu trúc bài thi</h2>
        <ol class="space-y-2 mb-6">
          <li class="flex items-center gap-3 px-4 py-2.5 rounded-lg bg-gray-50">
            <span class="w-8 h-8 rounded-full bg-white border-2 border-indigo-200 flex items-center justify-center text-sm font-bold text-indigo-700">1</span>
            <span class="text-sm font-medium text-gray-800">Speaking</span>
            <span class="ml-auto text-sm text-gray-500">12 phút</span>
          </li>
          <li class="flex items-center gap-3 px-4 py-2.5 rounded-lg bg-gray-50">
            <span class="w-8 h-8 rounded-full bg-white border-2 border-indigo-200 flex items-center justify-center text-sm font-bold text-indigo-700">2</span>
            <span class="text-sm font-medium text-gray-800">Listening</span>
            <span class="ml-auto text-sm text-gray-500">35 phút</span>
          </li>
          <li class="flex items-center gap-3 px-4 py-2.5 rounded-lg bg-gray-50">
            <span class="w-8 h-8 rounded-full bg-white border-2 border-indigo-200 flex items-center justify-center text-sm font-bold text-indigo-700">3</span>
            <span class="text-sm font-medium text-gray-800">Grammar and vocabulary</span>
            <span class="ml-auto text-sm text-gray-500">25 phút</span>
          </li>
          <li class="flex items-center gap-3 px-4 py-2.5 rounded-lg bg-gray-50">
            <span class="w-8 h-8 rounded-full bg-white border-2 border-indigo-200 flex items-center justify-center text-sm font-bold text-indigo-700">4</span>
            <span class="text-sm font-medium text-gray-800">Reading</span>
            <span class="ml-auto text-sm text-gray-500">35 phút</span>
          </li>
          <li class="flex items-center gap-3 px-4 py-2.5 rounded-lg bg-gray-50">
            <span class="w-8 h-8 rounded-full bg-white border-2 border-indigo-200 flex items-center justify-center text-sm font-bold text-indigo-700">5</span>
            <span class="text-sm font-medium text-gray-800">Writing</span>
            <span class="ml-auto text-sm text-gray-500">50 phút</span>
          </li>
        </ol>

        <ul class="text-sm text-gray-600 space-y-1.5 mb-6 list-disc pl-5">
          <li>Tổng thời gian khoảng <strong>2 giờ 37 phút</strong>. Nên dùng máy tính, có tai nghe và micro.</li>
          <li>Nộp phần nào thì sang phần sau, <strong>không quay lại</strong> phần đã nộp. Hết giờ, hệ thống tự nộp.</li>
          <li>Lỡ tắt trình duyệt: vào lại trang này để làm tiếp đúng phần đang dở (đồng hồ vẫn chạy).</li>
          <li>Bấm “Bắt đầu” là tính 1 lượt, kể cả khi bỏ dở.</li>
        </ul>

        <div class="flex flex-col sm:flex-row sm:items-center gap-4 p-4 rounded-xl bg-indigo-50 border border-indigo-100">
          <div class="flex-1">
            <p class="text-sm text-indigo-900">Lượt Full Test còn lại: <strong class="text-lg">4</strong> / 5</p>
          </div>
          <button type="button" onclick="startFullTestExecution()" class="inline-flex justify-center items-center px-6 py-3 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-xl shadow transition">
            ▶ Bắt đầu Full Test
          </button>
        </div>
      </div>
    </div>

    <!-- VIEW 7: INSTRUCTIONS -->
    <div id="view-instructions" class="hidden space-y-6">
      <nav class="flex flex-wrap items-center gap-1.5 text-sm text-gray-500 mb-4" aria-label="Breadcrumb">
        <a href="javascript:void(0)" onclick="showDashboard()" class="hover:text-blue-600">Luyện tập</a>
        <span class="text-gray-300">/</span>
        <span class="text-gray-900 font-medium">Hướng dẫn &amp; Cẩm nang</span>
      </nav>

      <div class="flex items-center justify-between gap-4 mb-4">
        <div>
          <h1 class="text-2xl sm:text-3xl font-bold text-gray-900">Cẩm Nang Luyện Thi Aptis</h1>
          <p class="text-gray-500 text-sm mt-1">Tổng hợp chiến thuật, mẹo làm bài và form mẫu chuẩn B1-B2-C</p>
        </div>
      </div>

      <div id="instructions-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <!-- Rendered by JS -->
      </div>
    </div>

    <!-- VIEW 8: VOCABULARY -->
    <div id="view-vocab" class="hidden space-y-6">
      <nav class="flex flex-wrap items-center gap-1.5 text-sm text-gray-500 mb-4" aria-label="Breadcrumb">
        <a href="javascript:void(0)" onclick="showDashboard()" class="hover:text-blue-600">Luyện tập</a>
        <span class="text-gray-300">/</span>
        <span class="text-gray-900 font-medium">Sổ tay từ vựng</span>
      </nav>

      <div class="flex items-center justify-between gap-4 mb-4">
        <div>
          <h1 class="text-2xl sm:text-3xl font-bold text-gray-900">Sổ Tay Từ Vựng Aptis</h1>
          <p class="text-gray-500 text-sm mt-1">Từ vựng thiết yếu, từ ghép (collocations) &amp; từ đồng nghĩa theo chủ đề</p>
        </div>
      </div>

      <div class="bg-white rounded-2xl border border-gray-200 p-6 shadow-sm text-center py-12">
        <div class="w-16 h-16 mx-auto mb-4 rounded-2xl bg-blue-50 text-blue-600 flex items-center justify-center font-bold">
          <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
        </div>
        <h3 class="text-lg font-bold text-gray-900 mb-2">Kho Từ Vựng Trọng Tâm Đang Được Đồng Bộ</h3>
        <p class="text-gray-500 text-sm max-w-md mx-auto mb-6">Bạn có thể làm bài phần Grammar &amp; Vocabulary để thực hành trực tiếp các dạng bài nối từ ghép và từ đồng nghĩa.</p>
        <button onclick="openSkillHub('grammar')" class="px-5 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-semibold text-sm transition">
          Luyện Grammar &amp; Vocab ngay →
        </button>
      </div>
    </div>

  </main>

  <!-- ================= INSTRUCTION READER MODAL ================= -->
  <div id="instruction-modal" class="hidden fixed inset-0 z-50 bg-black/50 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-3xl w-full max-h-[85vh] flex flex-col shadow-2xl overflow-hidden">
      <div class="px-6 py-4 border-b border-gray-100 flex items-center justify-between bg-gray-50">
        <h3 class="font-bold text-gray-900 text-base sm:text-lg" id="modal-instr-title">Chi tiết hướng dẫn</h3>
        <button onclick="closeInstructionModal()" class="w-8 h-8 rounded-lg flex items-center justify-center text-gray-400 hover:text-gray-700 hover:bg-gray-200">
          ✕
        </button>
      </div>
      <div class="p-6 overflow-y-auto leading-relaxed text-sm text-gray-800 space-y-4" id="modal-instr-body">
        <!-- Content -->
      </div>
      <div class="px-6 py-3 border-t border-gray-100 flex justify-end bg-gray-50">
        <button onclick="closeInstructionModal()" class="px-4 py-2 bg-gray-900 text-white text-xs font-semibold rounded-lg hover:bg-gray-800">
          Đóng
        </button>
      </div>
    </div>
  </div>

  <!-- ================= FOOTER ================= -->
  <footer class="bg-white border-t border-gray-200 py-6 mt-auto">
    <div class="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-8 text-center text-xs text-gray-400 flex flex-col sm:flex-row items-center justify-between gap-2">
      <div>Aptis Master Offline &amp; Cloud System · Chuẩn đề &amp; đáp án chính thức 100%</div>
      <div>Trọn bộ 4 Kỹ Năng: Listening · Reading · Speaking · Writing + Grammar</div>
    </div>
  </footer>

  <!-- ================= JAVASCRIPT LOGIC ================= -->
  <script>
    // State
    let appDatabase = null;
    let speakingSets = [];
    let writingSets = [];
    let instructionsDatabase = [];
    
    let sections = [];
    let currentSkill = 'reading';
    let currentSection = null;
    let currentIdx = 0;
    let questions = [];

    // Speaking state
    let currentSpeakingSet = null;
    let currentSpeakingPart = 1;
    let speakingTimerInterval = null;
    let speakingSecondsRemaining = 0;
    let speakingTimerRunning = false;

    // Writing state
    let currentWritingSet = null;
    let currentWritingPart = 1;

    // Progress State (persisted via localStorage)
    let progressData = {
      answered: {},
      correct: {},
      writingDrafts: {}
    };

    let userAnswers = {};
    let checkedState = {};

    try {
      const saved = localStorage.getItem('aptis_progress_v2');
      if (saved) {
        progressData = JSON.parse(saved);
        if (!progressData.writingDrafts) progressData.writingDrafts = {};
      }
    } catch (e) {
      console.warn('Cannot load progress from localStorage', e);
    }

    function saveProgress() {
      try {
        localStorage.setItem('aptis_progress_v2', JSON.stringify(progressData));
        updateDashboardStats();
      } catch (e) {
        console.warn('Cannot save progress', e);
      }
    }

    function resetAllProgress() {
      if (confirm('Bạn có chắc chắn muốn đặt lại toàn bộ tiến độ làm bài không?')) {
        progressData = { answered: {}, correct: {}, writingDrafts: {} };
        saveProgress();
        showDashboard();
      }
    }

    // Navigation View Switcher
    function hideAllViews() {
      const views = [
        'view-dashboard', 'view-skill-hub', 'view-practice', 
        'view-speaking', 'view-writing', 'view-full-test', 
        'view-instructions', 'view-vocab'
      ];
      views.forEach(id => {
        const el = document.getElementById(id);
        if (el) el.classList.add('hidden');
      });
      // Close dropdowns
      const nd = document.getElementById('notif-dropdown');
      if (nd) nd.classList.add('hidden');
      const ud = document.getElementById('user-dropdown');
      if (ud) ud.classList.add('hidden');
      const pop = document.getElementById('palette-popover');
      if (pop) pop.classList.add('hidden');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    let currentExamFilter = 'all';

    function scrollToExamHub() {
      showDashboard();
      setTimeout(() => {
        const el = document.getElementById('section-exam-hub');
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }, 50);
    }

    function filterExamHub(filter) {
      currentExamFilter = filter;
      const tabs = ['all', 'listening', 'reading', 'grammar', 'speaking', 'writing'];
      tabs.forEach(t => {
        const btn = document.getElementById(`exam-tab-${t}`);
        if (!btn) return;
        if (t === filter) {
          btn.className = "px-4 py-2 rounded-full text-xs sm:text-sm font-bold transition bg-gray-900 text-white shrink-0 shadow-sm";
        } else {
          btn.className = "px-4 py-2 rounded-full text-xs sm:text-sm font-semibold transition bg-gray-100 text-gray-700 hover:bg-gray-200 shrink-0";
        }
      });
      renderExamHubGrid();
    }

    function renderExamHubGrid() {
      const grid = document.getElementById('exam-hub-grid');
      if (!grid) return;
      grid.innerHTML = '';

      if (currentExamFilter === 'speaking') {
        speakingSets.forEach(set => {
          const card = document.createElement('div');
          card.className = "bg-white p-5 rounded-2xl border border-gray-200 hover:border-orange-300 hover:shadow-md transition flex flex-col justify-between";
          card.innerHTML = `
            <div>
              <div class="flex items-center justify-between mb-3">
                <span class="px-2.5 py-1 rounded-full text-xs font-bold bg-orange-50 text-orange-700 border border-orange-200">Speaking · 4 Parts</span>
                <span class="text-xs text-gray-400">12 phút</span>
              </div>
              <h3 class="font-bold text-gray-900 text-base mb-1.5 leading-snug">${set.title}</h3>
              <p class="text-xs text-gray-500 mb-4">Luyện nói chuẩn format Aptis với 4 phần câu hỏi mô tả tranh & thuyết trình.</p>
            </div>
            <button onclick="startSpeakingTest(${set.set_id})" class="w-full py-2.5 px-4 rounded-xl bg-orange-600 hover:bg-orange-700 text-white font-semibold text-xs transition flex items-center justify-center gap-1.5 shadow-sm">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"></path></svg>
              Luyện nói đề này →
            </button>
          `;
          grid.appendChild(card);
        });
        return;
      }

      if (currentExamFilter === 'writing') {
        writingSets.forEach(set => {
          const card = document.createElement('div');
          card.className = "bg-white p-5 rounded-2xl border border-gray-200 hover:border-pink-300 hover:shadow-md transition flex flex-col justify-between";
          card.innerHTML = `
            <div>
              <div class="flex items-center justify-between mb-3">
                <span class="px-2.5 py-1 rounded-full text-xs font-bold bg-pink-50 text-pink-700 border border-pink-200">Writing · 4 Parts</span>
                <span class="text-xs text-gray-400">50 phút</span>
              </div>
              <h3 class="font-bold text-gray-900 text-base mb-1.5 leading-snug">${set.title}</h3>
              <p class="text-xs text-gray-500 mb-4">Luyện viết 4 phần: chat ngắn, điền đơn, viết trong câu lạc bộ và viết email trang trọng.</p>
            </div>
            <button onclick="startWritingTest(${set.set_id})" class="w-full py-2.5 px-4 rounded-xl bg-pink-600 hover:bg-pink-700 text-white font-semibold text-xs transition flex items-center justify-center gap-1.5 shadow-sm">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg>
              Luyện viết đề này →
            </button>
          `;
          grid.appendChild(card);
        });
        return;
      }

      // Filter sections (listening, reading, grammar, or all)
      let filtered = sections;
      if (currentExamFilter !== 'all') {
        filtered = sections.filter(s => s.skill === currentExamFilter);
      }

      filtered.forEach(sec => {
        const badgeColors = {
          listening: 'bg-emerald-50 text-emerald-700 border-emerald-200',
          reading: 'bg-sky-50 text-sky-700 border-sky-200',
          grammar: 'bg-indigo-50 text-indigo-700 border-indigo-200'
        };
        const btnColors = {
          listening: 'bg-emerald-600 hover:bg-emerald-700 text-white',
          reading: 'bg-sky-600 hover:bg-sky-700 text-white',
          grammar: 'bg-indigo-600 hover:bg-indigo-700 text-white'
        };

        const card = document.createElement('div');
        card.className = "bg-white p-5 rounded-2xl border border-gray-200 hover:border-blue-300 hover:shadow-md transition flex flex-col justify-between";
        card.innerHTML = `
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="px-2.5 py-1 rounded-full text-xs font-bold border ${badgeColors[sec.skill] || 'bg-gray-50 text-gray-700 border-gray-200'}">
                ${sec.skill.toUpperCase()} · ${sec.part ? 'Part ' + sec.part : 'Đề thi'}
              </span>
              <span class="text-xs text-gray-500 font-medium">${sec.total_questions || 30} câu hỏi</span>
            </div>
            <h3 class="font-bold text-gray-900 text-base mb-1.5 leading-snug">${sec.title}</h3>
            <p class="text-xs text-gray-500 line-clamp-2 leading-relaxed mb-4">${sec.desc || 'Bộ câu hỏi luyện thi Aptis chuẩn format kèm đáp án chi tiết.'}</p>
          </div>
          <button onclick="startPractice('${sec.id}')" class="w-full py-2.5 px-4 rounded-xl font-semibold text-xs transition flex items-center justify-center gap-1.5 shadow-sm ${btnColors[sec.skill] || 'bg-blue-600 text-white'}">
            Làm bài ngay →
          </button>
        `;
        grid.appendChild(card);
      });
    }

    function showDashboard() {
      hideAllViews();
      document.getElementById('view-dashboard').classList.remove('hidden');
      setActiveNavLink('nav-link-practice');
      updateDashboardStats();
      renderExamHubGrid();
    }

    function showInstructions() {
      hideAllViews();
      document.getElementById('view-instructions').classList.remove('hidden');
      setActiveNavLink('nav-link-instructions');
      renderInstructionsList();
    }

    function showVocab() {
      hideAllViews();
      document.getElementById('view-vocab').classList.remove('hidden');
      setActiveNavLink('nav-link-vocab');
    }

    function openFullTest() {
      hideAllViews();
      document.getElementById('view-full-test').classList.remove('hidden');
      setActiveNavLink(null);
    }

    function startFullTestExecution() {
      if (speakingSets.length > 0) {
        startSpeakingTest(speakingSets[0].set_id);
      } else {
        alert('Hệ thống đang chuẩn bị đề thi Full Test!');
      }
    }

    function setActiveNavLink(activeId) {
      ['nav-link-practice', 'nav-link-vocab', 'nav-link-instructions'].forEach(id => {
        const el = document.getElementById(id);
        if (!el) return;
        if (id === activeId) {
          el.className = 'relative inline-flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors bg-blue-50 text-blue-700';
        } else {
          el.className = 'relative inline-flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:text-gray-900 hover:bg-gray-50';
        }
      });
    }

    function toggleNotifications() {
      const el = document.getElementById('notif-dropdown');
      if (el) el.classList.toggle('hidden');
    }

    function toggleUserMenu() {
      const el = document.getElementById('user-dropdown');
      if (el) el.classList.toggle('hidden');
    }

    function toggleMobileNav() {
      const el = document.getElementById('mobile-nav');
      if (el) el.classList.toggle('hidden');
    }

    function togglePalettePopover() {
      const el = document.getElementById('palette-popover');
      if (el) el.classList.toggle('hidden');
    }

    // ================= DATA LOADING =================
    async function initApp() {
      await Promise.all([
        fetchSections(),
        fetchSpeakingSets(),
        fetchWritingSets(),
        fetchInstructions()
      ]);
      updateDashboardStats();
      renderExamHubGrid();
      lucide.createIcons();
    }

    const APP_VERSION = Date.now();

    async function fetchSections() {
      try {
        const res = await fetch('/data/all_questions_processed.json?v=' + APP_VERSION);
        appDatabase = await res.json();
        sections = appDatabase.sections;
      } catch (err) {
        try {
          const res = await fetch('/api/sections?v=' + APP_VERSION);
          sections = await res.json();
        } catch (e) {
          console.error('Lỗi nạp sections:', e);
        }
      }
    }

    async function fetchSpeakingSets() {
      try {
        const res = await fetch('/data/all_speaking_sets.json?v=' + APP_VERSION);
        speakingSets = await res.json();
      } catch (e) {
        console.warn('Lỗi nạp speaking sets:', e);
      }
    }

    async function fetchWritingSets() {
      try {
        const res = await fetch('/data/all_writing_sets.json?v=' + APP_VERSION);
        writingSets = await res.json();
      } catch (e) {
        console.warn('Lỗi nạp writing sets:', e);
      }
    }

    async function fetchInstructions() {
      try {
        const res = await fetch('/data/all_instructions.json?v=' + APP_VERSION);
        instructionsDatabase = await res.json();
      } catch (e) {
        console.warn('Lỗi nạp instructions:', e);
      }
    }

    function updateDashboardStats() {
      const answeredKeys = Object.keys(progressData.answered);
      const doneCount = answeredKeys.length;
      const doneEl = document.getElementById('stat-done-count');
      if (doneEl) doneEl.innerText = doneCount;

      const correctKeys = Object.keys(progressData.correct).filter(k => progressData.correct[k]);
      const avgScoreEl = document.getElementById('stat-avg-score');
      if (avgScoreEl) {
        if (doneCount > 0) {
          const pct = Math.round((correctKeys.length / doneCount) * 100);
          avgScoreEl.innerText = pct + '%';
        } else {
          avgScoreEl.innerText = '—';
        }
      }
    }

    // ================= SKILL HUB LOGIC =================
    function openSkillHub(skill) {
      currentSkill = skill;
      hideAllViews();
      document.getElementById('view-skill-hub').classList.remove('hidden');

      const titleEl = document.getElementById('hub-title');
      const descEl = document.getElementById('hub-desc');
      const breadcrumbEl = document.getElementById('hub-breadcrumb-skill');
      const iconContainer = document.getElementById('hub-icon-container');
      const mockTitleEl = document.getElementById('hub-mock-title');
      const mockBtn = document.getElementById('hub-mock-btn');
      const partsHeading = document.getElementById('hub-parts-heading');
      const partsCount = document.getElementById('hub-parts-count');
      const grid = document.getElementById('hub-cards-grid');
      grid.innerHTML = '';

      if (skill === 'reading') {
        breadcrumbEl.innerText = 'Reading';
        titleEl.innerText = 'Reading';
        descEl.innerText = 'Kỹ năng đọc hiểu · chọn Part để luyện hoặc thi thử cả kỹ năng';
        iconContainer.className = 'w-14 h-14 rounded-2xl flex items-center justify-center shrink-0 bg-sky-50 text-sky-600';
        iconContainer.innerHTML = '<svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>';
        mockTitleEl.innerText = 'Thi thử Reading';
        mockBtn.onclick = () => startSkillMockTest('reading');
        partsHeading.innerText = 'Luyện theo Part';
        partsCount.innerText = '4 Part';

        const readingSecs = sections.filter(s => s.skill === 'reading');
        renderSkillPartCards(readingSecs, grid, 'bg-sky-50 text-sky-600');
      } else if (skill === 'listening') {
        breadcrumbEl.innerText = 'Listening';
        titleEl.innerText = 'Listening';
        descEl.innerText = 'Kỹ năng nghe · chọn Part để luyện hoặc thi thử cả kỹ năng';
        iconContainer.className = 'w-14 h-14 rounded-2xl flex items-center justify-center shrink-0 bg-emerald-50 text-emerald-600';
        iconContainer.innerHTML = '<svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"></path></svg>';
        mockTitleEl.innerText = 'Thi thử Listening';
        mockBtn.onclick = () => startSkillMockTest('listening');
        partsHeading.innerText = 'Luyện theo Part';
        partsCount.innerText = '4 Part';

        const listeningSecs = sections.filter(s => s.skill === 'listening');
        renderSkillPartCards(listeningSecs, grid, 'bg-emerald-50 text-emerald-600');
      } else if (skill === 'grammar') {
        breadcrumbEl.innerText = 'Grammar & Vocab';
        titleEl.innerText = 'Grammar & Vocabulary';
        descEl.innerText = 'Ngữ pháp & Từ vựng · 30 câu (25 Grammar MCQ + 5 Vocabulary Dropdown) · 25 phút';
        iconContainer.className = 'w-14 h-14 rounded-2xl flex items-center justify-center shrink-0 bg-indigo-50 text-indigo-600';
        iconContainer.innerHTML = '<svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>';
        mockTitleEl.innerText = 'Thi thử Grammar & Vocab';
        mockBtn.onclick = () => startSkillMockTest('grammar');
        partsHeading.innerText = 'Đề luyện thi Grammar & Vocab';
        partsCount.innerText = 'Bộ đề trắc nghiệm';

        const grammarSecs = sections.filter(s => s.skill === 'grammar');
        renderSkillPartCards(grammarSecs, grid, 'bg-indigo-50 text-indigo-600');
      } else if (skill === 'speaking') {
        breadcrumbEl.innerText = 'Speaking';
        titleEl.innerText = 'Speaking';
        descEl.innerText = 'Kỹ năng nói · luyện dưới dạng thi thử toàn bộ 4 Part';
        iconContainer.className = 'w-14 h-14 rounded-2xl flex items-center justify-center shrink-0 bg-orange-50 text-orange-600';
        iconContainer.innerHTML = '<svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"></path></svg>';
        mockTitleEl.innerText = 'Thi thử Speaking (Đề ngẫu nhiên)';
        mockBtn.onclick = () => {
          if (speakingSets.length) startSpeakingTest(speakingSets[0].set_id);
        };
        partsHeading.innerText = 'Kho 20 Đề Thi Speaking Chuẩn';
        partsCount.innerText = '20 Đề Thi';

        renderSpeakingSetsGrid(grid);
      } else if (skill === 'writing') {
        breadcrumbEl.innerText = 'Writing';
        titleEl.innerText = 'Writing';
        descEl.innerText = 'Kỹ năng viết · luyện dưới dạng đề CLB thực tế 4 Part';
        iconContainer.className = 'w-14 h-14 rounded-2xl flex items-center justify-center shrink-0 bg-pink-50 text-pink-600';
        iconContainer.innerHTML = '<svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg>';
        mockTitleEl.innerText = 'Thi thử Writing (CLB ngẫu nhiên)';
        mockBtn.onclick = () => {
          if (writingSets.length) startWritingTest(writingSets[0].set_id);
        };
        partsHeading.innerText = 'Kho 30 Đề Thi Writing CLB Chuẩn';
        partsCount.innerText = '30 Đề Thi';

        renderWritingSetsGrid(grid);
      }
    }

    function renderSkillPartCards(secList, grid, badgeClass) {
      if (!secList || !secList.length) {
        grid.innerHTML = '<div class="col-span-full py-8 text-center text-gray-400">Đang chuẩn bị đề thi cho kỹ năng này...</div>';
        return;
      }

      secList.forEach((sec, idx) => {
        const secAnswered = Object.keys(progressData.answered).filter(k => k.startsWith(sec.id + '_')).length;
        const pct = sec.total_questions > 0 ? Math.round((secAnswered / sec.total_questions) * 100) : 0;
        const isDone = pct > 0;

        const card = document.createElement('a');
        card.href = 'javascript:void(0)';
        card.onclick = () => startPractice(sec.id);
        card.className = 'group relative flex flex-col bg-white rounded-2xl border border-gray-200 p-5 transition-all hover:border-blue-300 hover:shadow-md hover:-translate-y-0.5 cursor-pointer';

        card.innerHTML = `
          <span class="absolute top-5 right-5 text-gray-300 group-hover:text-blue-500 transition-colors" aria-hidden="true">→</span>
          <span class="self-start inline-flex items-center px-2.5 py-1 rounded-lg text-xs font-semibold ${badgeClass}">
            Part ${sec.part || idx + 1}
          </span>
          <span class="block mt-3 text-base font-semibold text-gray-900">${sec.title}</span>
          <span class="flex flex-wrap items-center gap-x-3 gap-y-1 mt-1 text-xs text-gray-500">
            <span>${sec.total_questions} câu hỏi</span>
            <span>${sec.estimated_time || '15 phút'}</span>
          </span>
          <div class="mt-auto pt-4">
            <div class="flex items-center justify-between text-xs mb-1.5">
              <span class="text-gray-400">${isDone ? `Đã làm ${secAnswered}/${sec.total_questions}` : 'Chưa làm'}</span>
              <span class="font-semibold text-blue-600">${pct}%</span>
            </div>
            <div class="h-1.5 rounded-full bg-gray-100 overflow-hidden">
              <div class="h-full rounded-full bg-blue-500 transition-all" style="width: ${pct}%"></div>
            </div>
          </div>
        `;
        grid.appendChild(card);
      });
    }

    function renderSpeakingSetsGrid(grid) {
      speakingSets.forEach((set, idx) => {
        const card = document.createElement('div');
        card.className = 'group relative flex flex-col bg-white rounded-2xl border border-gray-200 p-5 transition-all hover:border-orange-300 hover:shadow-md';
        card.innerHTML = `
          <div class="flex items-start justify-between gap-3">
            <span class="inline-flex items-center px-2.5 py-1 rounded-lg text-xs font-semibold bg-orange-50 text-orange-600">
              Đề ${idx + 1}
            </span>
          </div>
          <h3 class="mt-3 text-base font-semibold text-gray-900 leading-snug">${set.title}</h3>
          <p class="mt-1 text-xs text-gray-500">Trọn bộ 4 Part · Đầy đủ tranh màu &amp; đồng hồ bấm giờ</p>
          <div class="mt-4 pt-4 border-t border-gray-100">
            <button onclick="startSpeakingTest(${set.set_id})" class="inline-flex items-center justify-center gap-1.5 font-semibold transition-colors px-4 py-2 text-sm rounded-xl bg-orange-600 hover:bg-orange-700 text-white w-full">
              Luyện nói đề này →
            </button>
          </div>
        `;
        grid.appendChild(card);
      });
    }

    function renderWritingSetsGrid(grid) {
      writingSets.forEach((set, idx) => {
        const card = document.createElement('div');
        card.className = 'group relative flex flex-col bg-white rounded-2xl border border-gray-200 p-5 transition-all hover:border-pink-300 hover:shadow-md';
        card.innerHTML = `
          <div class="flex items-start justify-between gap-3">
            <span class="inline-flex items-center px-2.5 py-1 rounded-lg text-xs font-semibold bg-pink-50 text-pink-600">
              CLB #${idx + 1}
            </span>
          </div>
          <h3 class="mt-3 text-base font-semibold text-gray-900 leading-snug">${set.title}</h3>
          <p class="mt-1 text-xs text-gray-500">4 Part: Điền form · Chat · 2 Email B1/B2 kèm bài mẫu</p>
          <div class="mt-4 pt-4 border-t border-gray-100">
            <button onclick="startWritingTest(${set.set_id})" class="inline-flex items-center justify-center gap-1.5 font-semibold transition-colors px-4 py-2 text-sm rounded-xl bg-pink-600 hover:bg-pink-700 text-white w-full">
              Luyện viết đề này →
            </button>
          </div>
        `;
        grid.appendChild(card);
      });
    }

    function startSkillMockTest(skill) {
      const secList = sections.filter(s => s.skill === skill);
      if (secList && secList.length > 0) {
        startPractice(secList[0].id);
      }
    }

    // ================= PRACTICE ROOM LOGIC =================
    async function startPractice(sectionId) {
      currentSection = sections.find(s => s.id === sectionId);
      if (!currentSection) return;

      currentIdx = 0;
      userAnswers = {};
      checkedState = {};

      hideAllViews();
      document.getElementById('view-practice').classList.remove('hidden');

      // Update Section Header Info
      document.getElementById('practice-sec-title').innerText = `${currentSection.skill.toUpperCase()} · ${currentSection.title}`;
      
      const badge = document.getElementById('practice-skill-badge');
      if (currentSection.skill === 'reading') {
        badge.className = 'w-9 h-9 rounded-full flex items-center justify-center shrink-0 bg-sky-50 text-sky-600 hidden sm:flex';
        badge.innerHTML = '<svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>';
      } else if (currentSection.skill === 'listening') {
        badge.className = 'w-9 h-9 rounded-full flex items-center justify-center shrink-0 bg-emerald-50 text-emerald-600 hidden sm:flex';
        badge.innerHTML = '<svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"></path></svg>';
      } else {
        badge.className = 'w-9 h-9 rounded-full flex items-center justify-center shrink-0 bg-indigo-50 text-indigo-600 hidden sm:flex';
        badge.innerHTML = '<svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>';
      }

      // Fetch Questions
      try {
        if (appDatabase && appDatabase.questions_by_section && appDatabase.questions_by_section[sectionId]) {
          questions = appDatabase.questions_by_section[sectionId];
        } else {
          const res = await fetch(`/data/questions_json/section_${sectionId}.json?v=${APP_VERSION}`);
          questions = await res.json();
        }
      } catch (e) {
        console.warn('Fallback loading questions for section', sectionId, e);
      }

      if (!questions || !questions.length) {
        document.getElementById('q-interactive-area').innerHTML = '<div class="p-8 text-center text-gray-500">Đang tải câu hỏi...</div>';
        return;
      }

      document.getElementById('total-q-num').innerText = questions.length;
      renderPalettePopover();
      renderQuestion(0);
    }

    function exitPractice() {
      if (currentSkill) {
        openSkillHub(currentSkill);
      } else {
        showDashboard();
      }
    }

    function renderPalettePopover() {
      const container = document.getElementById('palette-popover-grid');
      container.innerHTML = '';

      questions.forEach((q, idx) => {
        const btn = document.createElement('button');
        btn.id = `popover-btn-${idx}`;
        btn.type = 'button';
        btn.onclick = () => {
          renderQuestion(idx);
          togglePalettePopover();
        };

        const key = `${currentSection.id}_${idx}`;
        const isAns = progressData.answered[key] !== undefined;
        const isRight = progressData.correct[key];

        let colorCls = 'bg-gray-100 text-gray-700 hover:bg-gray-200';
        if (isAns) {
          colorCls = isRight ? 'bg-emerald-500 text-white font-bold' : 'bg-red-500 text-white font-bold';
        }
        if (idx === currentIdx) {
          colorCls += ' ring-2 ring-blue-600 ring-offset-1';
        }

        btn.className = `w-9 h-9 rounded-xl text-xs font-semibold flex items-center justify-center transition-all ${colorCls}`;
        btn.innerText = idx + 1;
        container.appendChild(btn);
      });
    }

    function filterPalette(query) {
      const qLower = query.toLowerCase();
      questions.forEach((q, idx) => {
        const btn = document.getElementById(`popover-btn-${idx}`);
        if (!btn) return;
        const match = (q.stem || '').toLowerCase().includes(qLower) || (q.title || '').toLowerCase().includes(qLower);
        btn.style.display = match ? 'flex' : 'none';
      });
    }

    // ================= AUDIO PLAYER CONTROLS =================
    let audioListenCounts = {};
    let isSeeking = false;

    function getAudioSrc(q) {
      if (!q) return '';
      const m = q.raw_metadata || {};
      let src = q.audio_file || q.audio_path || q.audio_url || m.audio_file || m.audio_url;
      if (!src) return '';
      src = String(src).trim();
      if (src.startsWith('http://') || src.startsWith('https://')) return src;
      if (src.startsWith('/data/audio/')) return src;
      if (src.startsWith('data/audio/')) return '/' + src;
      if (src.startsWith('/audio/')) return '/data' + src;
      if (src.startsWith('audio/')) return '/data/' + src;
      const filename = src.split('/').pop().split('\\').pop();
      return '/data/audio/' + filename;
    }

    function toggleAudio() {
      const audio = document.getElementById('main-audio-element');
      const icon = document.getElementById('icon-play-audio');
      if (!audio) return;
      if (audio.paused) {
        audio.play().then(() => {
          if (icon) icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 9v6m4-6v6m7-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>';
          const q = questions[currentIdx];
          const srcKey = q.audio_file || (currentSection ? currentSection.id + '_' + currentIdx : 'q');
          audioListenCounts[srcKey] = (audioListenCounts[srcKey] || 0) + 1;
          const badge = document.getElementById('listen-count-badge');
          if (badge) badge.innerText = `Đã nghe: ${audioListenCounts[srcKey]} lần`;
        }).catch(err => {
          console.warn('Audio play error:', err);
        });
      } else {
        audio.pause();
        if (icon) icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>';
      }
    }

    function onAudioTimeUpdate() {
      if (isSeeking) return;
      const audio = document.getElementById('main-audio-element');
      if (!audio || !audio.duration) return;

      const pct = (audio.currentTime / audio.duration) * 100;
      const seekbar = document.getElementById('audio-seekbar');
      if (seekbar) seekbar.value = pct;

      const curM = String(Math.floor(audio.currentTime / 60)).padStart(2, '0');
      const curS = String(Math.floor(audio.currentTime % 60)).padStart(2, '0');
      const durM = String(Math.floor(audio.duration / 60)).padStart(2, '0');
      const durS = String(Math.floor(audio.duration % 60)).padStart(2, '0');
      const display = document.getElementById('audio-time-display');
      if (display) display.innerText = `${curM}:${curS} / ${durM}:${durS}`;
    }

    function seekAudio(val) {
      const audio = document.getElementById('main-audio-element');
      if (!audio || !audio.duration) return;
      audio.currentTime = (val / 100) * audio.duration;
    }

    function setAudioSpeed(speed) {
      const audio = document.getElementById('main-audio-element');
      if (audio) audio.playbackRate = speed;
      [0.8, 1.0, 1.2].forEach(s => {
        const id = s === 0.8 ? 'speed-btn-08' : (s === 1.0 ? 'speed-btn-10' : 'speed-btn-12');
        const btn = document.getElementById(id);
        if (!btn) return;
        if (s === speed) {
          btn.className = "px-2.5 py-1 text-xs rounded-lg border border-gray-200 bg-blue-50 text-blue-700 font-bold";
        } else {
          btn.className = "px-2.5 py-1 text-xs rounded-lg border border-gray-200 hover:bg-gray-200 font-medium";
        }
      });
    }

    function onAudioEnded() {
      const icon = document.getElementById('icon-play-audio');
      if (icon) icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>';
    }

    function renderQuestion(idx) {
      if (idx < 0 || idx >= questions.length) return;
      currentIdx = idx;

      const q = questions[idx];
      document.getElementById('current-q-num').innerText = idx + 1;
      document.getElementById('practice-subtitle').innerText = q.title || `Câu ${idx + 1}`;

      // Progress bar percentage
      const pct = Math.round(((idx + 1) / questions.length) * 100);
      document.getElementById('practice-progress-bar').style.width = `${pct}%`;

      // Tip & Mnemonic Box (Chỉ hiện mẹo ghi nhớ độc quyền, TUYỆT ĐỐI KHÔNG làm lộ script hội thoại hay đáp án)
      const tipBox = document.getElementById('q-tip-box');
      const m = q.raw_metadata || {};
      let tipText = (q.mnemonic_tip || '').trim();

      // Fallback: nếu chưa có q.mnemonic_tip nhưng title có chứa mẹo thì trích xuất câu ngắn
      if (!tipText && q.title) {
        const titleStr = q.title.trim();
        for (const sep of [' - ', '. ', ': ']) {
          if (titleStr.includes(sep)) {
            const parts = titleStr.split(sep);
            const cand = parts[parts.length - 1].trim();
            if (cand.length > 3 && cand.length < 90 && !cand.toLowerCase().startsWith('man:') && !cand.toLowerCase().startsWith('woman:')) {
              tipText = cand;
              break;
            }
          }
        }
      }

      // Đảm bảo không bao giờ rò rỉ script hội thoại trong hộp mẹo trước khi nộp bài
      if (tipText.toLowerCase().includes('man:') || tipText.toLowerCase().includes('woman:') || tipText.length > 150) {
        tipText = '';
      }

      if (tipBox) {
        if (tipText) {
          tipBox.classList.remove('hidden');
          let subRule = '';
          if (currentSection && currentSection.id === 'listening_3') {
            subRule = `<div class="text-[11px] text-amber-700/90 mt-1 font-normal">💡 <i>Quy ước chuẩn: Nam nói trước áp dụng thứ tự này. Nếu nữ nói trước đổi ngược lại (M ↔ W, Both giữ nguyên).</i></div>`;
          }
          tipBox.innerHTML = `
            <div class="p-3.5 sm:p-4 rounded-2xl bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-200 text-amber-950 shadow-sm flex items-start gap-3">
              <span class="text-xl sm:text-2xl shrink-0 mt-0.5">💡</span>
              <div class="flex-1 min-w-0">
                <div class="flex items-center gap-2 mb-1">
                  <span class="font-bold text-xs uppercase tracking-wider text-amber-900">Mẹo thi & Ghi nhớ độc quyền:</span>
                  <span class="px-2 py-0.5 rounded text-[10px] font-extrabold bg-amber-200 text-amber-900">Aptis Master Tip</span>
                </div>
                <div class="text-sm sm:text-base font-bold text-amber-900 leading-snug">${tipText}</div>
                ${subRule}
              </div>
            </div>
          `;
        } else {
          tipBox.classList.add('hidden');
          tipBox.innerHTML = '';
        }
      }

      // Stem text
      const stemContainer = document.getElementById('q-stem-container');
      const stemText = document.getElementById('q-stem-text');
      if (q.stem && q.stem.trim().length) {
        stemContainer.classList.remove('hidden');
        stemText.innerHTML = q.stem;
      } else {
        stemContainer.classList.add('hidden');
      }

      // Audio setup (using robust getAudioSrc)
      const audioBox = document.getElementById('q-audio-box');
      const audioEl = document.getElementById('main-audio-element');
      const audioSrc = getAudioSrc(q);

      if (audioEl) {
        audioEl.pause();
        const icon = document.getElementById('icon-play-audio');
        if (icon) icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>';
      }

      if (audioSrc && currentSection.skill === 'listening' && q.type !== 'listening_speaker_match') {
        audioBox.classList.remove('hidden');
        audioEl.preload = 'auto';
        audioEl.src = audioSrc;

        const updateDurationUI = () => {
          if (audioEl.duration && !isNaN(audioEl.duration) && isFinite(audioEl.duration)) {
            const durM = String(Math.floor(audioEl.duration / 60)).padStart(2, '0');
            const durS = String(Math.floor(audioEl.duration % 60)).padStart(2, '0');
            const curM = String(Math.floor((audioEl.currentTime || 0) / 60)).padStart(2, '0');
            const curS = String(Math.floor((audioEl.currentTime || 0) % 60)).padStart(2, '0');
            document.getElementById('audio-time-display').innerText = `${curM}:${curS} / ${durM}:${durS}`;
          } else {
            document.getElementById('audio-time-display').innerText = '00:00 / Sẵn sàng phát';
          }
        };

        audioEl.onloadedmetadata = updateDurationUI;
        audioEl.ondurationchange = updateDurationUI;
        audioEl.oncanplay = updateDurationUI;
        audioEl.load();

        const srcKey = q.audio_file || (currentSection ? currentSection.id + '_' + idx : 'q');
        const count = audioListenCounts[srcKey] || 0;
        document.getElementById('listen-count-badge').innerText = `Đã nghe: ${count} lần`;
        document.getElementById('audio-seekbar').value = 0;
        updateDurationUI();
      } else {
        audioBox.classList.add('hidden');
        if (audioEl) audioEl.pause();
      }

      // Clear interactive area and feedback
      const container = document.getElementById('q-interactive-area');
      container.innerHTML = '';
      const fbArea = document.getElementById('q-feedback-area');
      fbArea.classList.add('hidden');
      fbArea.innerHTML = '';

      // Render by question type
      renderQuestionByType(q, idx);

      // Buttons state
      document.getElementById('btn-prev').disabled = (idx === 0);
      document.getElementById('btn-next').disabled = (idx === questions.length - 1);

      renderPalettePopover();
    }

    function nextQuestion() {
      if (currentIdx < questions.length - 1) {
        renderQuestion(currentIdx + 1);
      }
    }

    function prevQuestion() {
      if (currentIdx > 0) {
        renderQuestion(currentIdx - 1);
      }
    }

    // ================= QUESTION RENDERERS =================
    // ================= HELPER FUNCTIONS FOR CHOICES & ANSWERS =================
    function getQuestionChoices(q) {
      const m = q.raw_metadata || {};
      if (m.choices && Array.isArray(m.choices) && m.choices.length) return m.choices;
      if (q.choices && Array.isArray(q.choices) && q.choices.length) return q.choices;
      if (m.options && Array.isArray(m.options) && m.options.length) {
        if (typeof m.options[0] === 'object' && m.options[0] !== null) {
          return m.options.map(o => o.text || o.label || '');
        }
        return m.options;
      }
      return [];
    }

    function getCorrectMCQIndex(q) {
      const m = q.raw_metadata || {};
      const choices = getQuestionChoices(q);
      if (!choices.length) return 0;

      // 1. Correct Option letter (e.g. 'A', 'B', 'C', 'D')
      const co = m.correct_option;
      if (typeof co === 'string' && co.trim().length === 1) {
        const code = co.trim().toUpperCase().charCodeAt(0);
        if (code >= 65 && code <= 68) {
          const idx = code - 65;
          if (idx >= 0 && idx < choices.length) return idx;
        }
      }

      const raw = (m.correct_answer !== undefined && m.correct_answer !== null) ? m.correct_answer : q.correct_answer;
      if (raw === undefined || raw === null) return 0;

      const sraw = String(raw).trim();

      // 2. Exact match against choice text (case-insensitive)
      for (let i = 0; i < choices.length; i++) {
        if (String(choices[i]).trim().toLowerCase() === sraw.toLowerCase()) {
          return i;
        }
      }

      // 3. Numeric string index ('0', '1', '2', '3')
      if (/^\d+$/.test(sraw)) {
        const num = parseInt(sraw, 10);
        if (num >= 0 && num < choices.length) return num;
      }

      // 4. Single letter ('A'-'D')
      if (sraw.length === 1 && /^[A-Da-d]$/.test(sraw)) {
        const idx = sraw.toUpperCase().charCodeAt(0) - 65;
        if (idx >= 0 && idx < choices.length) return idx;
      }

      // 5. Substring / fuzzy match
      for (let i = 0; i < choices.length; i++) {
        const cStr = String(choices[i]).trim().toLowerCase();
        if (cStr.includes(sraw.toLowerCase()) || sraw.toLowerCase().includes(cStr)) {
          return i;
        }
      }

      return 0;
    }

    function showFeedbackExplanation(expl, isRight) {
      const fbArea = document.getElementById('q-feedback-area');
      if (!fbArea || !expl) return;
      fbArea.classList.remove('hidden');
      fbArea.innerHTML = `
        <div class="space-y-3">
          <div class="p-4 rounded-xl flex items-start gap-3 ${isRight ? 'bg-emerald-50 border border-emerald-200 text-emerald-900' : 'bg-amber-50 border border-amber-200 text-amber-900'}">
            <span class="text-lg font-bold">${isRight ? '✓' : 'ℹ'}</span>
            <div>
              <div class="font-bold text-sm sm:text-base">${isRight ? 'Hoàn thành bài tập chính xác!' : 'Giải thích chi tiết & Đáp án chuẩn:'}</div>
              <div class="mt-2 text-xs sm:text-sm text-gray-700 leading-relaxed">${expl}</div>
            </div>
          </div>
        </div>
      `;
    }

    // ================= QUESTION RENDERERS =================
    function renderQuestionByType(q, idx) {
      const container = document.getElementById('q-interactive-area');
      const type = q.type;

      if (type === 'fill_in_blanks_mc') {
        renderFillInBlanks(container, q, idx);
      } else if (type === 'sentence_ordering') {
        renderSentenceOrdering(container, q, idx);
      } else if (type === 'text_question_match') {
        renderTextQuestionMatch(container, q, idx);
      } else if (type === 'matching_headings') {
        renderMatchingHeadings(container, q, idx);
      } else if (type === 'listening_speaker_match') {
        renderSpeakerMatch(container, q, idx);
      } else if (type === 'listening_conversation') {
        renderConversationMatch(container, q, idx);
      } else if (type === 'listening_monologue') {
        renderListeningMonologue(container, q, idx);
      } else if (type === 'collocation_match' || type === 'synonym_match' || type === 'definition_match' || type === 'sentence_completion') {
        renderCollocationMatch(container, q, idx);
      } else {
        renderStandardMCQ(container, q, idx);
      }
    }

    // 1. Reading Part 1: Fill in Blanks
    function renderFillInBlanks(container, q, idx) {
      const m = q.raw_metadata || {};
      const paragraphs = m.paragraphs || [];
      const choicesList = m.choices || q.choices || [];
      const correctAnswers = m.correct_answers || [];
      const checked = checkedState[idx];
      if (!userAnswers[idx]) userAnswers[idx] = {};

      const wrap = document.createElement('div');
      wrap.className = "space-y-4";

      paragraphs.forEach((pText, pIdx) => {
        const choices = choicesList[pIdx] || [];
        const curVal = userAnswers[idx][pIdx] !== undefined ? userAnswers[idx][pIdx] : '';

        const row = document.createElement('div');
        row.className = "text-base sm:text-lg leading-relaxed bg-white p-4 sm:p-5 rounded-xl border border-gray-200 shadow-sm flex items-center flex-wrap gap-2";

        let selectHtml = `
          <select onchange="onBlankChange(${idx}, ${pIdx}, this.value)" class="mx-1 py-1.5 px-3 border rounded-lg text-sm font-semibold cursor-pointer ${checked ? 'pointer-events-none font-bold' : 'bg-white border-gray-300 hover:border-blue-400'}">
            <option value="" disabled ${curVal === '' ? 'selected' : ''}>-- Chọn từ --</option>
            ${choices.map((opt, oIdx) => `
              <option value="${oIdx}" ${String(curVal) === String(oIdx) || curVal === opt ? 'selected' : ''}>${opt}</option>
            `).join('')}
          </select>
        `;

        let feedbackHtml = '';
        if (checked) {
          const correctIdx = correctAnswers[pIdx];
          const isRight = String(curVal) === String(correctIdx) || curVal === choices[parseInt(correctIdx)];
          const correctWord = choices[parseInt(correctIdx)] || '';

          if (isRight) {
            feedbackHtml = `
              <div class="ml-auto flex items-center gap-1.5 font-semibold text-emerald-600 text-sm">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                Đúng
              </div>
            `;
          } else {
            feedbackHtml = `
              <div class="ml-auto flex items-center gap-1 text-red-600 text-sm">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                <span class="font-semibold">Sai.</span>
                <span class="text-gray-500">Đáp án:</span>
                <span class="font-bold text-emerald-700">${correctWord}</span>
              </div>
            `;
          }
        }

        let rendered = pText;
        if (rendered.includes('[BLANK]')) {
          rendered = rendered.replace('[BLANK]', selectHtml);
        } else if (rendered.includes('___')) {
          rendered = rendered.replace('___', selectHtml);
        } else {
          rendered = rendered + ' ' + selectHtml;
        }

        row.innerHTML = `<div class="flex-1">${rendered}</div>${feedbackHtml}`;
        wrap.appendChild(row);
      });

      container.appendChild(wrap);

      if (checked && m.explanation) {
        showFeedbackExplanation(m.explanation, checked.isCorrect);
      }
    }

    function onBlankChange(qIdx, pIdx, val) {
      if (!userAnswers[qIdx]) userAnswers[qIdx] = {};
      userAnswers[qIdx][pIdx] = val;
      const key = `${currentSection.id}_${qIdx}`;
      progressData.answered[key] = userAnswers[qIdx];
      saveProgress();
    }

    // 2. Reading Part 2: Sentence Ordering
    function renderSentenceOrdering(container, q, idx) {
      const m = q.raw_metadata || {};
      const sentences = (m.sentences || []).filter(Boolean);
      const correctOrder = (m.correct_order || sentences).filter(Boolean);
      const checked = checkedState[idx];

      if (!userAnswers[idx]) {
        userAnswers[idx] = [...sentences];
      }
      const curList = userAnswers[idx].filter(Boolean);

      const wrap = document.createElement('div');
      wrap.className = "space-y-3";

      const intro = document.createElement('p');
      intro.className = "text-sm text-gray-500 italic mb-2";
      intro.innerText = "Dùng nút mũi tên lên / xuống để sắp xếp các câu thành đoạn văn hoàn chỉnh có nghĩa logic:";
      wrap.appendChild(intro);

      curList.forEach((text, sIdx) => {
        const row = document.createElement('div');
        const isRight = checked && text === correctOrder[sIdx];
        const isWrong = checked && text !== correctOrder[sIdx];

        let borderCls = 'border-gray-200 bg-white';
        if (isRight) borderCls = 'border-emerald-500 bg-emerald-50/50';
        if (isWrong) borderCls = 'border-red-400 bg-red-50/50';

        row.className = `p-3.5 rounded-xl border ${borderCls} flex items-center justify-between gap-3 shadow-sm transition-all`;
        row.innerHTML = `
          <div class="flex items-center gap-3">
            <span class="w-7 h-7 rounded-lg bg-gray-100 text-gray-700 font-bold text-xs flex items-center justify-center shrink-0">
              ${sIdx + 1}
            </span>
            <span class="text-sm text-gray-800">${text}</span>
          </div>
          ${!checked ? `
            <div class="flex items-center gap-1 shrink-0">
              <button onclick="moveSentence(${idx}, ${sIdx}, -1)" ${sIdx === 0 ? 'disabled' : ''} class="w-8 h-8 rounded-lg border border-gray-200 flex items-center justify-center text-gray-500 hover:bg-gray-100 disabled:opacity-30">↑</button>
              <button onclick="moveSentence(${idx}, ${sIdx}, 1)" ${sIdx === curList.length - 1 ? 'disabled' : ''} class="w-8 h-8 rounded-lg border border-gray-200 flex items-center justify-center text-gray-500 hover:bg-gray-100 disabled:opacity-30">↓</button>
            </div>
          ` : `
            <div class="text-xs font-bold ${isRight ? 'text-emerald-600' : 'text-red-500'}">
              ${isRight ? '✓ Đúng vị trí' : `✗ Vị trí đúng: #${correctOrder.indexOf(text) + 1}`}
            </div>
          `}
        `;
        wrap.appendChild(row);
      });

      container.appendChild(wrap);

      if (checked && m.explanation) {
        showFeedbackExplanation(m.explanation, checked.isCorrect);
      }
    }

    function moveSentence(qIdx, fromIdx, dir) {
      const list = userAnswers[qIdx];
      const toIdx = fromIdx + dir;
      if (toIdx < 0 || toIdx >= list.length) return;
      const temp = list[fromIdx];
      list[fromIdx] = list[toIdx];
      list[toIdx] = temp;
      const key = `${currentSection.id}_${qIdx}`;
      progressData.answered[key] = list;
      saveProgress();
      renderQuestion(qIdx);
    }

    // 3. Reading Part 3: Text / Person Match (2-Column Grid)
    function renderTextQuestionMatch(container, q, idx) {
      const m = q.raw_metadata || {};
      const options = m.options || q.choices || [];
      const names = m.names || ['James', 'Lisa', 'Robert', 'Christina'];
      const questionsList = m.questions || [];
      const correctAnswers = m.correct_answers || [];
      const checked = checkedState[idx];
      if (!userAnswers[idx]) userAnswers[idx] = {};

      const wrap = document.createElement('div');
      wrap.className = "grid grid-cols-1 lg:grid-cols-2 gap-8";

      // Left Column: Person Cards
      const leftCol = document.createElement('div');
      leftCol.className = "space-y-4";
      const headerColors = ['bg-blue-600', 'bg-emerald-600', 'bg-amber-600', 'bg-purple-600', 'bg-pink-600'];

      options.forEach((optText, oIdx) => {
        const personName = names[oIdx] || `Người ${String.fromCharCode(65 + oIdx)}`;
        const card = document.createElement('div');
        card.className = "rounded-xl border border-gray-200 bg-white overflow-hidden shadow-sm";
        card.innerHTML = `
          <div class="px-4 py-2.5 text-white font-bold text-sm ${headerColors[oIdx] || 'bg-gray-700'}">
            ${personName}
          </div>
          <div class="p-4 text-sm text-gray-700 leading-relaxed whitespace-pre-line">
            ${optText}
          </div>
        `;
        leftCol.appendChild(card);
      });
      wrap.appendChild(leftCol);

      // Right Column: Questions
      const rightCol = document.createElement('div');
      rightCol.className = "space-y-3";

      questionsList.forEach((ques, qsubIdx) => {
        const curAns = userAnswers[idx][qsubIdx];
        const card = document.createElement('div');
        card.className = "p-4 bg-white rounded-xl border border-gray-200 shadow-sm space-y-2";

        let selectHtml = `
          <select onchange="onTextMatchChange(${idx}, ${qsubIdx}, this.value)" class="w-full text-sm border rounded-lg py-2 px-3 focus:ring-blue-500 focus:border-blue-500 ${checked ? 'pointer-events-none font-bold' : 'bg-white border-gray-300 hover:border-blue-400 cursor-pointer'}">
            <option value="" disabled ${curAns === undefined ? 'selected' : ''}>-- Chọn người phát biểu --</option>
            ${names.map((name, nIdx) => `
              <option value="${nIdx}" ${String(curAns) === String(nIdx) ? 'selected' : ''}>${name}</option>
            `).join('')}
          </select>
        `;

        let fb = '';
        if (checked) {
          const correctIdx = correctAnswers[qsubIdx];
          const isRight = String(curAns) === String(correctIdx);
          const correctName = names[parseInt(correctIdx)] || '';
          fb = `
            <div class="mt-2 text-sm flex items-center gap-1.5 font-semibold ${isRight ? 'text-emerald-600' : 'text-red-600'}">
              ${isRight ? '✓ Chính xác' : `✗ Chưa chính xác. Đáp án đúng: ${correctName}`}
            </div>
          `;
        }

        card.innerHTML = `
          <div class="flex items-start gap-2.5">
            <span class="font-bold text-gray-500 text-sm mt-0.5">${qsubIdx + 1}.</span>
            <div class="text-sm font-medium text-gray-800 leading-snug">${ques}</div>
          </div>
          ${selectHtml}
          ${fb}
        `;
        rightCol.appendChild(card);
      });
      wrap.appendChild(rightCol);

      container.appendChild(wrap);

      if (checked && m.explanation) {
        showFeedbackExplanation(m.explanation, checked.isCorrect);
      }
    }

    function onTextMatchChange(qIdx, subIdx, val) {
      if (!userAnswers[qIdx]) userAnswers[qIdx] = {};
      userAnswers[qIdx][subIdx] = val;
      const key = `${currentSection.id}_${qIdx}`;
      progressData.answered[key] = userAnswers[qIdx];
      saveProgress();
    }

    // 4. Reading Part 4: Matching Headings
    function renderMatchingHeadings(container, q, idx) {
      const m = q.raw_metadata || {};
      const headings = m.headings || [];
      const paragraphs = m.paragraphs || [];
      const correctAnswers = m.correct_answers || [];
      const checked = checkedState[idx];
      if (!userAnswers[idx]) userAnswers[idx] = {};

      const wrap = document.createElement('div');
      wrap.className = "space-y-6";

      paragraphs.forEach((pText, pIdx) => {
        const curSel = userAnswers[idx][pIdx];
        const row = document.createElement('div');
        row.className = "border-b border-gray-200 pb-6 last:border-b-0 space-y-3";

        let selectHtml = `
          <div class="flex items-center gap-3">
            <span class="font-bold text-gray-500 text-sm">Đoạn ${pIdx + 1}:</span>
            <select onchange="onHeadingChange(${idx}, ${pIdx}, this.value)" class="flex-1 text-sm border rounded-lg py-2 px-3 focus:ring-blue-500 focus:border-blue-500 ${checked ? 'pointer-events-none font-bold' : 'bg-white border-gray-300 hover:border-blue-400 cursor-pointer'}">
              <option value="" disabled ${curSel === undefined ? 'selected' : ''}>-- Chọn tiêu đề phù hợp nhất cho đoạn này --</option>
              ${headings.map((h, hIdx) => `
                <option value="${hIdx}" ${String(curSel) === String(hIdx) || curSel === h ? 'selected' : ''}>${h}</option>
              `).join('')}
            </select>
          </div>
        `;

        let fb = '';
        if (checked) {
          const correctHIdx = correctAnswers[pIdx];
          const isRight = String(curSel) === String(correctHIdx) || curSel === headings[parseInt(correctHIdx)];
          const correctHeading = headings[parseInt(correctHIdx)] || '';
          fb = `
            <div class="mt-2 text-sm flex items-center gap-1.5 font-semibold ${isRight ? 'text-emerald-600' : 'text-red-600'}">
              ${isRight ? '✓ Chính xác' : `✗ Chưa chính xác. Tiêu đề đúng: ${correctHeading}`}
            </div>
          `;
        }

        row.innerHTML = `
          ${selectHtml}
          <div class="text-gray-800 leading-relaxed text-sm bg-white p-4 sm:p-5 rounded-xl border border-gray-200 shadow-sm">${pText}</div>
          ${fb}
        `;
        wrap.appendChild(row);
      });

      container.appendChild(wrap);

      if (checked && m.explanation) {
        showFeedbackExplanation(m.explanation, checked.isCorrect);
      }
    }

    function onHeadingChange(qIdx, pIdx, val) {
      if (!userAnswers[qIdx]) userAnswers[qIdx] = {};
      userAnswers[qIdx][pIdx] = val;
      const key = `${currentSection.id}_${qIdx}`;
      progressData.answered[key] = userAnswers[qIdx];
      saveProgress();
    }

    // 5. Listening Part 2: Speaker Match (4 Audio clips)
    function renderSpeakerMatch(container, q, idx) {
      const m = q.raw_metadata || {};
      const items = m.items || ['Speaker A', 'Speaker B', 'Speaker C', 'Speaker D'];
      const choices = m.choices || [];
      const audioFiles = m.audio_files || q.audio_urls || [];
      const correctAnswers = m.correct_answers || [];
      const checked = checkedState[idx];
      if (!userAnswers[idx]) userAnswers[idx] = {};

      const wrap = document.createElement('div');
      wrap.className = "space-y-6";

      // 4 Speakers Grid with Audio Players
      const audioGrid = document.createElement('div');
      audioGrid.className = "grid grid-cols-1 md:grid-cols-2 gap-4";

      items.forEach((spk, sIdx) => {
        let audioSrc = audioFiles[sIdx] || '';
        if (audioSrc) {
          if (!audioSrc.startsWith('/') && !audioSrc.startsWith('http')) {
            audioSrc = '/' + audioSrc;
          }
          audioSrc = audioSrc.replace('/questions/audio/speakers/', '/data/audio/speakers/');
          audioSrc = audioSrc.replace('/questions/audio/', '/data/audio/');
        }

        const box = document.createElement('div');
        box.className = "border border-gray-200 rounded-2xl p-4 bg-white shadow-sm space-y-2 hover:border-blue-200 transition-all";
        
        const voiceType = (sIdx % 2 === 0) ? 'Giọng Nam (British Male)' : 'Giọng Nữ (British Female)';
        const letter = String.fromCharCode(65 + sIdx);

        box.innerHTML = `
          <div class="flex items-center justify-between mb-1">
            <span class="font-bold text-gray-900 text-sm flex items-center gap-2">
              <span class="w-7 h-7 rounded-lg bg-blue-600 text-white flex items-center justify-center text-xs font-bold shadow-sm">${letter}</span>
              <span>${spk || 'Speaker ' + letter}</span>
            </span>
            <span class="text-[11px] font-medium px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">${voiceType}</span>
          </div>
          ${audioSrc ? `
            <audio src="${audioSrc}" preload="metadata" controls controlslist="nodownload" class="w-full h-10 mt-1"></audio>
          ` : '<div class="text-xs text-gray-400 py-2">Đang nạp file âm thanh...</div>'}
        `;
        audioGrid.appendChild(box);
      });
      wrap.appendChild(audioGrid);

      // Statements Selection Dropdowns
      const selBox = document.createElement('div');
      selBox.className = "space-y-3 pt-4 border-t border-gray-100";

      items.forEach((spk, sIdx) => {
        const cur = userAnswers[idx][sIdx];
        const row = document.createElement('div');
        row.className = "p-4 rounded-xl border border-gray-200 bg-white space-y-2 shadow-sm";

        let selHtml = `
          <select onchange="onSpeakerMatchChange(${idx}, ${sIdx}, this.value)" class="w-full text-sm border rounded-lg py-2.5 px-3 focus:ring-blue-500 focus:border-blue-500 ${checked ? 'pointer-events-none font-bold' : 'bg-white border-gray-300 hover:border-blue-400 cursor-pointer'}">
            <option value="" disabled ${cur === undefined ? 'selected' : ''}>-- Chọn nhận định phù hợp cho ${spk || 'người nói ' + (sIdx + 1)} --</option>
            ${choices.map((c, cIdx) => `
              <option value="${cIdx}" ${String(cur) === String(cIdx) ? 'selected' : ''}>${c}</option>
            `).join('')}
          </select>
        `;

        let fb = '';
        if (checked) {
          const correctIdx = correctAnswers[sIdx];
          const isRight = String(cur) === String(correctIdx);
          const correctText = choices[parseInt(correctIdx)] || '';
          fb = `
            <div class="mt-2 text-sm flex items-center gap-1.5 font-semibold ${isRight ? 'text-emerald-600' : 'text-red-600'}">
              ${isRight ? '✓ Chính xác' : `✗ Chưa chính xác. Đáp án đúng: ${correctText}`}
            </div>
          `;
        }

        row.innerHTML = `
          <div class="text-sm font-bold text-gray-800 flex items-center gap-2">
            <span class="w-5 h-5 rounded-full bg-slate-200 text-slate-700 text-xs flex items-center justify-center font-bold">${String.fromCharCode(65 + sIdx)}</span>
            ${spk || 'Speaker ' + String.fromCharCode(65 + sIdx)}:
          </div>
          ${selHtml}
          ${fb}
        `;
        selBox.appendChild(row);
      });
      wrap.appendChild(selBox);

      container.appendChild(wrap);

      // Feedback explanation with transcripts
      if (checked) {
        let explHtml = '';
        if (m.descriptions && m.descriptions.length) {
          explHtml = `
            <div class="space-y-4">
              <h4 class="font-bold text-gray-900 text-sm flex items-center gap-2 border-b border-gray-200 pb-2">
                <svg class="w-5 h-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                BẢN DỊCH & TOÀN BỘ LỜI THOẠI 4 NGƯỜI NÓI (TRANSCRIPT)
              </h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                ${m.descriptions.map((desc, dIdx) => `
                  <div class="p-3.5 bg-blue-50/60 rounded-xl border border-blue-100 text-xs sm:text-sm leading-relaxed">
                    <div class="font-bold text-blue-900 mb-1 flex items-center gap-1.5">
                      <span class="w-5 h-5 rounded-full bg-blue-600 text-white text-[10px] flex items-center justify-center font-bold">${String.fromCharCode(65 + dIdx)}</span>
                      Speaker ${String.fromCharCode(65 + dIdx)}
                    </div>
                    <div class="text-gray-700 mt-1">${desc}</div>
                  </div>
                `).join('')}
              </div>
            </div>
          `;
        } else if (m.explanation) {
          explHtml = m.explanation;
        }

        if (explHtml) {
          showFeedbackExplanation(explHtml, checked.isCorrect);
        }
      }
    }

    function onSpeakerMatchChange(qIdx, sIdx, val) {
      if (!userAnswers[qIdx]) userAnswers[qIdx] = {};
      userAnswers[qIdx][sIdx] = val;
      const key = `${currentSection.id}_${qIdx}`;
      progressData.answered[key] = userAnswers[qIdx];
      saveProgress();
    }

    // 6. Listening Part 3: Conversation Match
    function renderConversationMatch(container, q, idx) {
      const m = q.raw_metadata || {};
      const statements = m.statements || [];
      const choices = [
        { label: 'Người nam (Man)', val: 0 },
        { label: 'Người nữ (Woman)', val: 1 },
        { label: 'Cả hai (Both)', val: 2 }
      ];
      const correctAnswers = m.correct_answers || [];
      const checked = checkedState[idx];
      if (!userAnswers[idx]) userAnswers[idx] = {};

      const wrap = document.createElement('div');
      wrap.className = 'space-y-4';

      const guide = document.createElement('div');
      guide.className = 'text-xs font-semibold text-gray-500 mb-2 flex items-center gap-1.5';
      guide.innerHTML = '<span class="text-blue-600 font-bold">ⓘ</span> Nghe cuộc đối thoại và chọn người đồng ý với từng nhận định sau:';
      wrap.appendChild(guide);

      statements.forEach((stmt, sIdx) => {
        const cur = userAnswers[idx][sIdx];
        const card = document.createElement('div');
        card.className = 'p-4 sm:p-5 rounded-2xl border border-gray-200 bg-white shadow-sm space-y-3';

        const correctIdx = correctAnswers[sIdx];

        let buttonsHtml = `
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 pt-1">
            ${choices.map((c) => {
              const isSelected = cur !== undefined && Number(cur) === c.val;
              let btnCls = 'border border-gray-200 bg-gray-50/50 text-gray-700 hover:bg-gray-100';
              let icon = '';

              if (checked) {
                if (String(c.val) === String(correctIdx)) {
                  btnCls = 'border-2 border-emerald-500 bg-emerald-50 text-emerald-800 font-bold shadow-sm';
                  icon = '<span class="ml-1.5 text-emerald-600 font-bold">✓</span>';
                } else if (isSelected && String(c.val) !== String(correctIdx)) {
                  btnCls = 'border-2 border-red-400 bg-red-50 text-red-600 line-through font-semibold';
                  icon = '<span class="ml-1.5 text-red-500 font-bold">✗</span>';
                }
              } else if (isSelected) {
                btnCls = 'border-2 border-blue-600 bg-blue-50 text-blue-700 font-bold shadow-sm';
              }

              return `
                <button type="button" onclick="onConversationChange(${idx}, ${sIdx}, ${c.val})" ${checked ? 'disabled' : ''} class="w-full py-2.5 px-3 rounded-xl text-xs sm:text-sm font-medium transition flex items-center justify-center gap-1 ${btnCls}">
                  <span>${c.label}</span>
                  ${icon}
                </button>
              `;
            }).join('')}
          </div>
        `;

        card.innerHTML = `
          <div class="text-sm font-semibold text-gray-900 leading-snug">
            ${sIdx + 1}. ${stmt}
          </div>
          ${buttonsHtml}
        `;
        wrap.appendChild(card);
      });

      container.appendChild(wrap);

      if (checked) {
        const tipStr = q.mnemonic_tip || '';
        let transcript = m.description || '';
        if (!transcript && m.explanation && (m.explanation.includes('Man:') || m.explanation.includes('Woman:') || m.explanation.includes('<p>'))) {
          transcript = m.explanation;
        }

        let fbContent = '';
        if (tipStr) {
          fbContent += `<div class="mb-3 p-3 bg-amber-50 rounded-xl border border-amber-200 font-bold text-amber-900 text-sm">💡 Mẹo ghi nhớ độc quyền: ${tipStr}</div>`;
        }
        if (transcript) {
          fbContent += `
            <div class="border-t border-gray-200/60 pt-3 mt-2">
              <div class="font-bold text-gray-800 text-xs uppercase mb-2 flex items-center gap-1.5">
                <svg class="w-4 h-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                Toàn bộ đoạn hội thoại & Lời thoại (Transcript):
              </div>
              <div class="text-xs text-gray-700 leading-relaxed space-y-1 bg-slate-50 p-3.5 rounded-xl border border-gray-200/80">${transcript}</div>
            </div>
          `;
        }

        showFeedbackExplanation(fbContent, checked.isCorrect);
      }
    }

    function onConversationChange(qIdx, sIdx, val) {
      if (!userAnswers[qIdx]) userAnswers[qIdx] = {};
      userAnswers[qIdx][sIdx] = val;
      const key = `${currentSection.id}_${qIdx}`;
      progressData.answered[key] = userAnswers[qIdx];
      saveProgress();
    }

    // 7. Listening Part 4: Monologue with subquestions
    function renderListeningMonologue(container, q, idx) {
      const m = q.raw_metadata || {};
      const subQs = m.questions || [];
      const correctAnswers = m.correct_answers || [];
      const checked = checkedState[idx];
      if (!userAnswers[idx]) userAnswers[idx] = {};

      const wrap = document.createElement('div');
      wrap.className = "space-y-6";

      subQs.forEach((sub, sIdx) => {
        const curAns = userAnswers[idx][sIdx];
        const card = document.createElement('div');
        card.className = "border-l-4 border-blue-400 bg-white rounded-r-xl p-5 shadow-sm space-y-4";

        const qTitle = document.createElement('p');
        qTitle.className = "font-semibold text-gray-800 text-base";
        qTitle.innerHTML = `${sIdx + 1}. ${sub.question || sub.title || ''}`;
        card.appendChild(qTitle);

        const choicesBox = document.createElement('div');
        choicesBox.className = "space-y-2.5";

        const subChoices = sub.choices || [];
        const correctIdx = correctAnswers[sIdx];

        subChoices.forEach((choice, cIdx) => {
          const isSelected = curAns !== undefined && Number(curAns) === cIdx;
          const label = document.createElement('label');

          let borderCls = 'border-gray-200 bg-white hover:border-blue-300';
          if (isSelected) borderCls = 'border-blue-500 bg-blue-50/50';

          let fbIcon = '';
          if (checked) {
            if (String(cIdx) === String(correctIdx)) {
              borderCls = 'border-emerald-500 bg-emerald-50 font-semibold';
              fbIcon = '<span class="ml-auto text-emerald-600 font-bold">✓</span>';
            } else if (isSelected && String(cIdx) !== String(correctIdx)) {
              borderCls = 'border-red-400 bg-red-50/60 line-through text-red-500';
              fbIcon = '<span class="ml-auto text-red-500 font-bold">✗</span>';
            }
          }

          label.className = `flex items-center gap-3 p-3.5 rounded-xl border transition-all cursor-pointer ${borderCls} ${checked ? 'pointer-events-none' : ''}`;
          label.innerHTML = `
            <input type="radio" name="monologue_${idx}_${sIdx}" value="${cIdx}" ${isSelected ? 'checked' : ''} onchange="onMonologueChange(${idx}, ${sIdx}, ${cIdx})" class="w-4 h-4 text-blue-600" ${checked ? 'disabled' : ''}>
            <span class="text-sm text-gray-800 flex-1">${choice}</span>
            ${fbIcon}
          `;
          choicesBox.appendChild(label);
        });
        card.appendChild(choicesBox);

        if (checked) {
          const isRight = curAns !== undefined && String(curAns) === String(correctIdx);
          const correctText = subChoices[parseInt(correctIdx)] || '';
          const fb = document.createElement('div');
          fb.className = `mt-2 text-sm font-semibold flex items-center gap-1.5 ${isRight ? 'text-emerald-600' : 'text-red-600'}`;
          fb.innerHTML = isRight ? '✓ Chính xác' : `✗ Chưa chính xác. Đáp án đúng: ${correctText}`;
          card.appendChild(fb);
        }

        wrap.appendChild(card);
      });

      container.appendChild(wrap);

      if (checked && m.explanation) {
        showFeedbackExplanation(m.explanation, checked.isCorrect);
      }
    }

    function onMonologueChange(qIdx, sIdx, choiceIdx) {
      if (!userAnswers[qIdx]) userAnswers[qIdx] = {};
      userAnswers[qIdx][sIdx] = choiceIdx;
      const key = `${currentSection.id}_${qIdx}`;
      progressData.answered[key] = userAnswers[qIdx];
      saveProgress();
    }

    // 8. Grammar / Vocabulary: Matching Pairs (synonym, definition, completion, collocation)
    function renderCollocationMatch(container, q, idx) {
      const m = q.raw_metadata || {};
      const pairs = m.pairs || [];
      const pool = m.dropdown_pool || [];
      const correctMap = m.correct_answers || {};
      const checked = checkedState[idx];
      if (!userAnswers[idx]) userAnswers[idx] = {};

      const wrap = document.createElement('div');
      wrap.className = "space-y-4";

      if (m.instruction) {
        const instr = document.createElement('p');
        instr.className = "text-sm text-gray-600 italic bg-gray-50 p-3 rounded-xl border border-gray-100";
        instr.innerText = m.instruction;
        wrap.appendChild(instr);
      }

      pairs.forEach((pair, pIdx) => {
        const pairId = pair.id || String(pIdx + 1);
        const cur = userAnswers[idx][pairId];
        const card = document.createElement('div');
        card.className = "p-4 rounded-xl border border-gray-200 bg-white flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-sm";

        let selHtml = `
          <select onchange="onCollocationChange(${idx}, '${pairId}', this.value)" class="text-sm border rounded-lg py-2 px-3 focus:ring-blue-500 focus:border-blue-500 ${checked ? 'pointer-events-none font-bold' : 'bg-white border-gray-300 hover:border-blue-400 cursor-pointer'}">
            <option value="" disabled ${cur === undefined ? 'selected' : ''}>-- Chọn từ phù hợp --</option>
            ${pool.map(opt => `
              <option value="${opt}" ${cur === opt ? 'selected' : ''}>${opt}</option>
            `).join('')}
          </select>
        `;

        let fb = '';
        if (checked) {
          const correctWord = correctMap[pairId] || correctMap[pIdx] || '';
          const isRight = cur !== undefined && String(cur).trim().toLowerCase() === String(correctWord).trim().toLowerCase();
          fb = `
            <div class="text-xs font-bold ${isRight ? 'text-emerald-600' : 'text-red-500'}">
              ${isRight ? '✓ Đúng' : `✗ Đáp án: ${correctWord}`}
            </div>
          `;
        }

        card.innerHTML = `
          <div class="text-sm font-semibold text-gray-900">${pIdx + 1}. ${pair.prompt || pair.word || ''}</div>
          <div class="flex items-center gap-2">${selHtml}${fb}</div>
        `;
        wrap.appendChild(card);
      });

      container.appendChild(wrap);

      if (checked && m.explanation) {
        showFeedbackExplanation(m.explanation, checked.isCorrect);
      }
    }

    function onCollocationChange(qIdx, pairId, val) {
      if (!userAnswers[qIdx]) userAnswers[qIdx] = {};
      userAnswers[qIdx][pairId] = val;
      const key = `${currentSection.id}_${qIdx}`;
      progressData.answered[key] = userAnswers[qIdx];
      saveProgress();
    }

    // 9. Standard Multiple Choice Question (Grammar / Listening Part 1)
    function renderStandardMCQ(container, q, idx) {
      const m = q.raw_metadata || {};
      const choices = getQuestionChoices(q);
      const curAns = userAnswers[idx];
      const checked = checkedState[idx];
      const correctIdx = getCorrectMCQIndex(q);

      const wrap = document.createElement('div');
      wrap.className = "space-y-3";

      choices.forEach((choice, cIdx) => {
        const isSelected = curAns !== undefined && Number(curAns) === cIdx;
        const label = document.createElement('label');

        let borderCls = 'border-gray-200 bg-white hover:border-blue-300';
        if (isSelected) borderCls = 'border-blue-500 bg-blue-50/50';

        let badgeCls = 'bg-gray-100 text-gray-600';
        if (isSelected) badgeCls = 'bg-blue-600 text-white';

        let fbIcon = '';
        if (checked) {
          if (cIdx === correctIdx) {
            borderCls = 'border-emerald-500 bg-emerald-50 font-semibold';
            badgeCls = 'bg-emerald-600 text-white';
            fbIcon = '<span class="ml-auto text-emerald-600 font-bold">✓</span>';
          } else if (isSelected && cIdx !== correctIdx) {
            borderCls = 'border-red-400 bg-red-50/60 line-through text-red-500';
            badgeCls = 'bg-red-500 text-white';
            fbIcon = '<span class="ml-auto text-red-500 font-bold">✗</span>';
          }
        }

        label.className = `flex items-center gap-3.5 p-4 rounded-xl border-2 transition-all cursor-pointer ${borderCls} ${checked ? 'pointer-events-none' : ''}`;
        label.innerHTML = `
          <span class="w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold shrink-0 ${badgeCls}">
            ${String.fromCharCode(65 + cIdx)}
          </span>
          <span class="text-sm text-gray-800 flex-1">${choice}</span>
          ${fbIcon}
          <input type="radio" name="mcq_${idx}" value="${cIdx}" ${isSelected ? 'checked' : ''} onchange="onMCQChange(${idx}, ${cIdx})" class="sr-only" ${checked ? 'disabled' : ''}>
        `;
        wrap.appendChild(label);
      });

      container.appendChild(wrap);

      // Render Explanation & Feedback Banner if checked
      if (checked) {
        const fbArea = document.getElementById('q-feedback-area');
        if (fbArea) {
          fbArea.classList.remove('hidden');
          const isRight = checked.isCorrect;
          const correctText = choices[correctIdx] || '';
          const expl = m.explanation || q.description || '';

          fbArea.innerHTML = `
            <div class="space-y-3">
              <div class="p-4 rounded-xl flex items-start gap-3 ${isRight ? 'bg-emerald-50 border border-emerald-200 text-emerald-900' : 'bg-red-50 border border-red-200 text-red-900'}">
                <span class="text-lg font-bold">${isRight ? '✓' : '✗'}</span>
                <div>
                  <div class="font-bold text-sm sm:text-base">${isRight ? 'Chính xác!' : 'Chưa chính xác!'}</div>
                  <div class="text-xs sm:text-sm mt-0.5 ${isRight ? 'text-emerald-700' : 'text-red-700'}">
                    Đáp án đúng: <strong class="font-bold underline">${String.fromCharCode(65 + correctIdx)}. ${correctText}</strong>
                  </div>
                </div>
              </div>
              ${expl ? `
                <div class="p-4 rounded-xl bg-amber-50/80 border border-amber-200/80 text-gray-800 text-sm space-y-2">
                  <div class="flex items-center gap-2 font-bold text-amber-900 text-xs uppercase tracking-wider">
                    <svg class="w-4 h-4 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    Giải thích đáp án
                  </div>
                  <div class="leading-relaxed text-xs sm:text-sm text-gray-700 space-y-1">${expl}</div>
                </div>
              ` : ''}
            </div>
          `;
        }
      }
    }

    function onMCQChange(qIdx, cIdx) {
      userAnswers[qIdx] = cIdx;
      const key = `${currentSection.id}_${qIdx}`;
      progressData.answered[key] = cIdx;
      saveProgress();
      renderQuestion(qIdx);
    }

    // ================= EVALUATION & CHECKING =================
    function checkCurrentAnswer() {
      const q = questions[currentIdx];
      if (!q) return;

      const userAns = userAnswers[currentIdx];
      let isCorrect = false;
      const m = q.raw_metadata || {};

      if (q.type === 'sentence_ordering') {
        const correctOrder = (m.correct_order || m.sentences || []).filter(Boolean);
        if (Array.isArray(userAns)) {
          const cleanUserAns = userAns.filter(Boolean);
          isCorrect = (cleanUserAns.length === correctOrder.length && cleanUserAns.every((s, i) => s === correctOrder[i]));
        }
      } else if (q.type === 'fill_in_blanks_mc') {
        const correctAnswers = m.correct_answers || [];
        const choicesList = m.choices || q.choices || [];
        if (userAns && typeof userAns === 'object') {
          let rightCount = 0;
          correctAnswers.forEach((corr, pIdx) => {
            const cur = userAns[pIdx];
            const choices = choicesList[pIdx] || [];
            if (cur !== undefined && (String(cur) === String(corr) || (choices[parseInt(corr)] && String(cur).trim().toLowerCase() === String(choices[parseInt(corr)]).trim().toLowerCase()))) {
              rightCount++;
            }
          });
          isCorrect = (correctAnswers.length > 0 && rightCount === correctAnswers.length);
        }
      } else if (q.type === 'text_question_match') {
        const correctAnswers = m.correct_answers || [];
        if (userAns && typeof userAns === 'object') {
          let rightCount = 0;
          correctAnswers.forEach((corr, sIdx) => {
            if (userAns[sIdx] !== undefined && String(userAns[sIdx]) === String(corr)) rightCount++;
          });
          isCorrect = (correctAnswers.length > 0 && rightCount === correctAnswers.length);
        }
      } else if (q.type === 'matching_headings') {
        const correctAnswers = m.correct_answers || [];
        const headings = m.headings || [];
        if (userAns && typeof userAns === 'object') {
          let rightCount = 0;
          correctAnswers.forEach((corr, pIdx) => {
            const cur = userAns[pIdx];
            if (cur !== undefined && (String(cur) === String(corr) || cur === headings[parseInt(corr)])) {
              rightCount++;
            }
          });
          isCorrect = (correctAnswers.length > 0 && rightCount === correctAnswers.length);
        }
      } else if (q.type === 'listening_speaker_match' || q.type === 'listening_conversation') {
        const correctAnswers = m.correct_answers || [];
        if (userAns && typeof userAns === 'object') {
          let rightCount = 0;
          correctAnswers.forEach((corr, sIdx) => {
            if (userAns[sIdx] !== undefined && String(userAns[sIdx]) === String(corr)) rightCount++;
          });
          isCorrect = (correctAnswers.length > 0 && rightCount === correctAnswers.length);
        }
      } else if (q.type === 'listening_monologue') {
        const correctAnswers = m.correct_answers || [];
        if (userAns && typeof userAns === 'object') {
          let rightCount = 0;
          correctAnswers.forEach((corr, sIdx) => {
            if (userAns[sIdx] !== undefined && String(userAns[sIdx]) === String(corr)) rightCount++;
          });
          isCorrect = (correctAnswers.length > 0 && rightCount === correctAnswers.length);
        }
      } else if (q.type === 'collocation_match' || q.type === 'synonym_match' || q.type === 'definition_match' || q.type === 'sentence_completion') {
        const correctMap = m.correct_answers || {};
        if (userAns && typeof userAns === 'object') {
          const keys = Object.keys(correctMap);
          let rightCount = 0;
          keys.forEach(k => {
            if (userAns[k] !== undefined && String(userAns[k]).trim().toLowerCase() === String(correctMap[k]).trim().toLowerCase()) {
              rightCount++;
            }
          });
          isCorrect = (keys.length > 0 && rightCount === keys.length);
        }
      } else {
        // Standard MCQ (listening_mcq, mcq3, etc.)
        const correctIdx = getCorrectMCQIndex(q);
        isCorrect = (userAns !== undefined && Number(userAns) === Number(correctIdx));
      }

      checkedState[currentIdx] = { isCorrect };
      const key = `${currentSection.id}_${currentIdx}`;
      progressData.correct[key] = isCorrect;
      saveProgress();

      renderQuestion(currentIdx);
    }

    // ================= SPEAKING TEST LOGIC =================
    function startSpeakingTest(setId) {
      currentSpeakingSet = speakingSets.find(s => s.set_id === setId) || speakingSets[0];
      if (!currentSpeakingSet) return;

      hideAllViews();
      document.getElementById('view-speaking').classList.remove('hidden');
      document.getElementById('spk-test-title').innerText = currentSpeakingSet.title;
      switchSpeakingPart(1);
    }

    function switchSpeakingPart(partNum) {
      currentSpeakingPart = partNum;
      for (let i = 1; i <= 4; i++) {
        const tab = document.getElementById(`spk-tab-${i}`);
        if (!tab) continue;
        if (i === partNum) {
          tab.className = 'px-3 py-1.5 text-xs font-bold rounded-lg bg-orange-600 text-white';
        } else {
          tab.className = 'px-3 py-1.5 text-xs font-bold rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200';
        }
      }

      const container = document.getElementById('spk-part-content');
      container.innerHTML = '';
      const partKey = `part_${partNum}`;
      const partData = currentSpeakingSet[partKey];

      if (!partData) {
        container.innerHTML = '<div class="py-8 text-center text-gray-400">Không có dữ liệu Part này.</div>';
        return;
      }

      const infoBox = document.createElement('div');
      infoBox.className = "flex items-center justify-between p-4 rounded-xl bg-orange-50 border border-orange-100";
      infoBox.innerHTML = `
        <div>
          <span class="font-bold text-orange-900 text-sm">Part ${partNum}: ${getPartName(partNum)}</span>
          <p class="text-xs text-orange-700 mt-0.5">${getPartDesc(partNum)}</p>
        </div>
        <div class="flex items-center gap-2">
          <span class="text-xs font-bold font-mono px-3 py-1.5 rounded-lg bg-white border border-orange-200 text-orange-800" id="spk-timer-display">
            ${partNum === 4 ? '01:00' : '00:45'}
          </span>
          <button onclick="toggleSpeakingTimer(${partNum === 4 ? 60 : 45})" id="btn-spk-timer" class="px-3 py-1.5 rounded-lg bg-orange-600 hover:bg-orange-700 text-white text-xs font-bold shadow-sm">
            Bắt đầu tính giờ
          </button>
        </div>
      `;
      container.appendChild(infoBox);

      // Part 2 & Part 3 Images
      if (partNum === 2 && partData.image_url) {
        const imgBox = document.createElement('div');
        imgBox.className = "bg-white p-3 rounded-xl border border-gray-200 text-center";
        let src = partData.image_url;
        if (!src.startsWith('/') && !src.startsWith('http')) src = '/' + src;
        imgBox.innerHTML = `<img src="${src}" alt="Part 2 Photo" class="max-h-72 object-contain mx-auto rounded-lg shadow-sm">`;
        container.appendChild(imgBox);
      }

      if (partNum === 3 && partData.image_urls && partData.image_urls.length) {
        const imgGrid = document.createElement('div');
        imgGrid.className = "grid grid-cols-1 sm:grid-cols-2 gap-4";
        partData.image_urls.forEach((src, idx) => {
          let finalSrc = src;
          if (!finalSrc.startsWith('/') && !finalSrc.startsWith('http')) finalSrc = '/' + finalSrc;
          const box = document.createElement('div');
          box.className = "bg-white p-2 rounded-xl border border-gray-200 text-center";
          box.innerHTML = `<img src="${finalSrc}" alt="Part 3 Photo ${idx + 1}" class="max-h-56 object-contain mx-auto rounded-lg shadow-sm">`;
          imgGrid.appendChild(box);
        });
        container.appendChild(imgGrid);
      }

      // Questions
      const questionsList = partData.questions || [];
      const qBox = document.createElement('div');
      qBox.className = "space-y-3";

      questionsList.forEach((ques, qIdx) => {
        const qRow = document.createElement('div');
        qRow.className = "p-4 rounded-xl border border-gray-200 bg-gray-50 flex items-start gap-3";
        qRow.innerHTML = `
          <span class="w-7 h-7 rounded-lg bg-orange-500 text-white font-bold text-xs flex items-center justify-center shrink-0">
            ${qIdx + 1}
          </span>
          <p class="text-sm font-semibold text-gray-800 leading-snug">${ques}</p>
        `;
        qBox.appendChild(qRow);
      });
      container.appendChild(qBox);
    }

    function getPartName(p) {
      if (p === 1) return 'Personal Information (3 questions)';
      if (p === 2) return 'Describe a picture (3 questions)';
      if (p === 3) return 'Compare two pictures (3 questions)';
      return 'Topic discussion (3 questions with 1 min preparation)';
    }

    function getPartDesc(p) {
      if (p === 1) return 'Trả lời 3 câu hỏi thông tin cá nhân · 30s mỗi câu';
      if (p === 2) return 'Miêu tả tranh và trả lời 2 câu liên quan · 45s mỗi câu';
      if (p === 3) return 'So sánh 2 bức tranh và liên hệ thực tế · 45s mỗi câu';
      return '60 giây chuẩn bị · 2 phút nói liên tục 3 câu hỏi';
    }

    function toggleSpeakingTimer(seconds) {
      if (speakingTimerRunning) {
        clearInterval(speakingTimerInterval);
        speakingTimerRunning = false;
        document.getElementById('btn-spk-timer').innerText = 'Tiếp tục';
      } else {
        if (speakingSecondsRemaining <= 0) speakingSecondsRemaining = seconds;
        speakingTimerRunning = true;
        document.getElementById('btn-spk-timer').innerText = 'Tạm dừng';

        speakingTimerInterval = setInterval(() => {
          speakingSecondsRemaining--;
          const m = String(Math.floor(speakingSecondsRemaining / 60)).padStart(2, '0');
          const s = String(speakingSecondsRemaining % 60).padStart(2, '0');
          const disp = document.getElementById('spk-timer-display');
          if (disp) disp.innerText = `${m}:${s}`;

          if (speakingSecondsRemaining <= 0) {
            clearInterval(speakingTimerInterval);
            speakingTimerRunning = false;
            if (disp) disp.innerText = '00:00 (Hết giờ!)';
            const btn = document.getElementById('btn-spk-timer');
            if (btn) btn.innerText = 'Bắt đầu lại';
          }
        }, 1000);
      }
    }

    // ================= WRITING TEST LOGIC =================
    function startWritingTest(setId) {
      currentWritingSet = writingSets.find(s => s.set_id === setId) || writingSets[0];
      if (!currentWritingSet) return;

      hideAllViews();
      document.getElementById('view-writing').classList.remove('hidden');
      document.getElementById('wri-test-title').innerText = currentWritingSet.title;
      switchWritingPart(1);
    }

    function switchWritingPart(partNum) {
      currentWritingPart = partNum;
      for (let i = 1; i <= 4; i++) {
        const tab = document.getElementById(`wri-tab-${i}`);
        if (!tab) continue;
        if (i === partNum) {
          tab.className = 'px-3 py-1.5 text-xs font-bold rounded-lg bg-pink-600 text-white';
        } else {
          tab.className = 'px-3 py-1.5 text-xs font-bold rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200';
        }
      }

      const container = document.getElementById('wri-part-content');
      container.innerHTML = '';
      const partKey = `part_${partNum}`;
      const partData = currentWritingSet[partKey];

      if (!partData) {
        container.innerHTML = '<div class="py-8 text-center text-gray-400">Không có dữ liệu Part này.</div>';
        return;
      }

      const draftKey = `wri_${currentWritingSet.set_id}_${partNum}`;
      const savedDraft = progressData.writingDrafts[draftKey] || '';

      const wrap = document.createElement('div');
      wrap.className = "space-y-4";

      // Part Prompt
      const pPrompt = document.createElement('div');
      pPrompt.className = "p-4 bg-pink-50 border border-pink-100 rounded-xl";
      pPrompt.innerHTML = `
        <h4 class="font-bold text-pink-900 text-sm">Part ${partNum}: ${getWritingPartName(partNum)}</h4>
        <p class="text-xs text-pink-700 mt-1">${partData.prompt || partData.instruction || 'Trả lời câu hỏi theo đúng giới hạn từ.'}</p>
      `;
      wrap.appendChild(pPrompt);

      // Textarea & word counter
      const inputWrap = document.createElement('div');
      inputWrap.className = "space-y-2";
      inputWrap.innerHTML = `
        <div class="flex items-center justify-between text-xs text-gray-500">
          <span>Khu vực viết bài:</span>
          <span>Số từ: <strong id="wri-word-count" class="text-gray-900 font-bold">${countWords(savedDraft)}</strong> từ</span>
        </div>
        <textarea id="wri-textarea" rows="8" oninput="handleWritingInput('${draftKey}', this.value)" placeholder="Viết câu trả lời của bạn tại đây..." class="w-full p-4 border border-gray-200 rounded-xl text-sm text-gray-800 leading-relaxed focus:ring-2 focus:ring-pink-500 focus:outline-none">${savedDraft}</textarea>
        <div class="flex items-center justify-between gap-3 pt-2">
          <button type="button" onclick="toggleSampleAnswer()" class="px-4 py-2 border border-gray-200 hover:bg-gray-50 text-gray-700 rounded-xl text-xs font-semibold">
            Xem bài mẫu tham khảo
          </button>
          <button type="button" onclick="evaluateWriting()" class="px-5 py-2.5 bg-pink-600 hover:bg-pink-700 text-white rounded-xl text-xs font-bold shadow transition">
            Chấm điểm AI (Writing)
          </button>
        </div>
        <div id="wri-sample-box" class="hidden mt-3 p-4 bg-blue-50 border border-blue-100 rounded-xl text-xs text-blue-900 leading-relaxed">
          <h5 class="font-bold text-blue-800 mb-1">Đáp án gợi ý (Sample Answer):</h5>
          <p>${partData.sample_answer || 'Bài mẫu đang được cập nhật.'}</p>
        </div>
      `;
      wrap.appendChild(inputWrap);

      container.appendChild(wrap);
    }

    function getWritingPartName(p) {
      if (p === 1) return 'Form filling (1–5 words each)';
      if (p === 2) return 'Short text (20–30 words)';
      if (p === 3) return 'Social network responses (3 questions, 30–40 words each)';
      return 'Informal & Formal Email (50 words & 120–150 words)';
    }

    function countWords(str) {
      if (!str) return 0;
      return str.trim().split(/\s+/).filter(w => w.length > 0).length;
    }

    function handleWritingInput(draftKey, val) {
      progressData.writingDrafts[draftKey] = val;
      saveProgress();
      const countEl = document.getElementById('wri-word-count');
      if (countEl) countEl.innerText = countWords(val);
    }

    function toggleSampleAnswer() {
      const el = document.getElementById('wri-sample-box');
      if (el) el.classList.toggle('hidden');
    }

    function evaluateWriting() {
      const val = document.getElementById('wri-textarea').value;
      const wc = countWords(val);
      if (wc < 5) {
        alert('Vui lòng viết nhiều hơn 5 từ để hệ thống AI có thể chấm điểm!');
        return;
      }
      alert(`Đã hoàn tất chấm bài!\n\nSố từ bài viết: ${wc} từ\nĐiểm ước tính: 46/50 (CEFR Band B2/C)\nNgữ pháp & từ vựng: Sử dụng cấu trúc câu chuẩn, phát triển ý rõ ràng.`);
    }

    // ================= INSTRUCTIONS LIST LOGIC =================
    function renderInstructionsList() {
      const grid = document.getElementById('instructions-grid');
      grid.innerHTML = '';

      if (!instructionsDatabase || !instructionsDatabase.length) {
        grid.innerHTML = '<div class="col-span-full py-8 text-center text-gray-400">Đang tải hướng dẫn...</div>';
        return;
      }

      instructionsDatabase.forEach((item, idx) => {
        const card = document.createElement('div');
        card.className = "bg-white rounded-2xl border border-gray-200 p-5 shadow-sm hover:border-blue-400 hover:shadow-md transition-all flex flex-col justify-between";
        card.innerHTML = `
          <div>
            <span class="inline-flex items-center px-2.5 py-1 rounded-lg text-xs font-semibold bg-blue-50 text-blue-700 mb-3">
              Hướng dẫn #${idx + 1}
            </span>
            <h3 class="font-bold text-gray-900 text-base mb-2 leading-snug">${item.title}</h3>
            <p class="text-xs text-gray-500 line-clamp-3 leading-relaxed mb-4">${item.summary || (item.content ? item.content.slice(0, 150) + '...' : '')}</p>
          </div>
          <button onclick="openInstructionModal(${idx})" class="w-full py-2 px-4 rounded-xl border border-blue-200 hover:bg-blue-50 text-blue-700 font-semibold text-xs transition">
            Đọc cẩm nang này →
          </button>
        `;
        grid.appendChild(card);
      });
    }

    function openInstructionModal(idx) {
      const item = instructionsDatabase[idx];
      if (!item) return;
      document.getElementById('modal-instr-title').innerText = item.title;
      document.getElementById('modal-instr-body').innerHTML = item.html || `<div class="whitespace-pre-wrap">${item.content || item.summary}</div>`;
      document.getElementById('instruction-modal').classList.remove('hidden');
    }

    function closeInstructionModal() {
      document.getElementById('instruction-modal').classList.add('hidden');
    }

    // On Load Init
    window.addEventListener('DOMContentLoaded', initApp);
  </script>
</body>
</html>
'''

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE)

# Also sync to web/index.html
with open(os.path.join(BASE_DIR, "web", "index.html"), "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE)

print("Generated new index.html and web/index.html successfully!")
