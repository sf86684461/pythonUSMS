// 表格页面批量优化工具
import fs from 'fs';
import path from 'path';

class TableOptimizer {
  constructor() {
    this.viewsPath = path.join(__dirname, '../views/modules');
    this.optimizedFiles = [];
  }

  // 获取所有需要优化的表格页面
  getAllTablePages() {
    const modules = fs.readdirSync(this.viewsPath);
    const tablePages = [];

    modules.forEach(module => {
      const modulePath = path.join(this.viewsPath, module);
      if (fs.statSync(modulePath).isDirectory()) {
        const listFile = path.join(modulePath, 'list.vue');
        if (fs.existsSync(listFile)) {
          tablePages.push(listFile);
        }
      }
    });

    return tablePages;
  }

  // 优化单个表格页面
  optimizeTablePage(filePath) {
    try {
      let content = fs.readFileSync(filePath, 'utf8');
      let modified = false;

      // 1. 添加现代化样式导入
      if (!content.includes('import tableStyleMixin')) {
        content = content.replace(
          /import AddOrUpdate from ["']\.\/add-or-update["'];/,
          `import AddOrUpdate from "./add-or-update";
import tableStyleMixin from '@/mixins/table-style-mixin.js';`
        );
        modified = true;
      }

      // 2. 添加mixins配置
      if (!content.includes('mixins: [tableStyleMixin]')) {
        content = content.replace(
          /components: \{[\s\S]*?\},/,
          (match) => `${match}
\t\tmixins: [tableStyleMixin],`
        );
        modified = true;
      }

      // 3. 替换表格容器的内联样式为CSS类
      content = content.replace(
        /:style='\{[^}]*"border":"1px solid #e9e9e9"[^}]*\}'/g,
        'class="table-container"'
      );

      // 4. 优化搜索表单样式
      content = content.replace(
        /class="center-form-pv"/g,
        'class="center-form-pv modern-search-form"'
      );

      // 5. 优化操作按钮区域样式
      content = content.replace(
        /class="actions"/g,
        'class="actions modern-actions"'
      );

      if (modified) {
        fs.writeFileSync(filePath, content, 'utf8');
        this.optimizedFiles.push(filePath);
        console.log(`✅ 优化完成: ${path.basename(filePath)}`);
      }

      return true;
    } catch (error) {
      console.error(`❌ 优化失败: ${path.basename(filePath)} - ${error.message}`);
      return false;
    }
  }

  // 批量优化所有表格页面
  optimizeAllTablePages() {
    console.log('🚀 开始批量优化表格页面...');
    
    const tablePages = this.getAllTablePages();
    console.log(`📋 找到 ${tablePages.length} 个表格页面`);

    let successCount = 0;
    let failCount = 0;

    tablePages.forEach(filePath => {
      if (this.optimizeTablePage(filePath)) {
        successCount++;
      } else {
        failCount++;
      }
    });

    console.log('\n📊 优化结果统计:');
    console.log(`✅ 成功: ${successCount} 个文件`);
    console.log(`❌ 失败: ${failCount} 个文件`);
    console.log(`📝 已优化文件列表:`);
    this.optimizedFiles.forEach(file => {
      console.log(`   - ${path.basename(file)}`);
    });

    return {
      success: successCount,
      failed: failCount,
      optimizedFiles: this.optimizedFiles
    };
  }

  // 生成优化报告
  generateOptimizationReport() {
    const report = {
      timestamp: new Date().toISOString(),
      optimizedFiles: this.optimizedFiles,
      optimizations: [
        '✨ 应用现代化表格样式',
        '🎨 优化搜索表单UI',
        '🔘 美化操作按钮',
        '📱 添加响应式设计',
        '⚡ 提升用户体验'
      ]
    };

    const reportPath = path.join(__dirname, '../reports/table-optimization-report.json');
    
    // 确保reports目录存在
    const reportsDir = path.dirname(reportPath);
    if (!fs.existsSync(reportsDir)) {
      fs.mkdirSync(reportsDir, { recursive: true });
    }

    fs.writeFileSync(reportPath, JSON.stringify(report, null, 2), 'utf8');
    console.log(`📄 优化报告已生成: ${reportPath}`);

    return report;
  }
}

// 使用示例
const optimizer = new TableOptimizer();

// 批量优化所有表格页面
// optimizer.optimizeAllTablePages();

// 生成优化报告
// optimizer.generateOptimizationReport();

export default TableOptimizer;